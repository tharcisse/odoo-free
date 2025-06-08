import logging
import brevo_python
from brevo_python.rest import ApiException
from odoo import models, fields, api, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


def get_contats(api_instance, **kwargs):
    api_response = None

    try:
        if not kwargs.get('is_company'):
            api_response = api_instance.get_contacts(
                **kwargs
            )
        else:
            api_response = api_instance.companies_get(
                **kwargs
            )
    except ApiException as e:
        raise UserError(
            "Exception when calling ContactsApi->get_contacts: %s\n" % e)
    return api_response


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'grev.brevo.mixin']

    brevoid = fields.Char()
    brevo_can_receive_email_campaigns = fields.Boolean(
        'Can receive email campaigns', default=True)
    brevo_can_receive_sms_campaigns = fields.Boolean(
        'Can receive sms campaigns', default=True)

    firstname = fields.Char(compute='_compute_name_details', store=True)
    lastname = fields.Char(compute='_compute_name_details', store=True)
    linkedin = fields.Char()

    @api.depends('name')
    def _compute_name_details(self):
        for rec in self:
            name_parts = []
            if rec.name:
                name_parts = rec.name.split(' ')
            if len(name_parts) > 1:
                rec.firstname = name_parts[0]
                rec.lastname = ' '.join(name_parts[1:])
            else:
                rec.firstname = rec.name
                rec.lastname = ''

    @api.model
    def process_brevo_to_odoo_contacts(self, contacts, is_company=False):
        for contact in contacts:
            contactid = str(contact.get('id'))
            contact_id = self.search([('brevoid', '=', contactid)])
            if not contact_id:
                contact_data = {
                    'email': contact.get('email'),
                    'brevoid': str(contact.get('id')),
                    'is_company': is_company,
                }
                if contact.get('attributes'):
                    contact_data.update(self._map_attributes(
                        contact.get('attributes')))
                if contact.get('linked_contacts_ids'):
                    child_ids = self.search(
                        [('brevoid', 'in', [str(id) for id in contact.get('linked_contacts_ids')])])
                    contact_data.update({'child_ids': [(6, 0, child_ids.ids)]})

                self.create(contact_data)

    def _get_brevo_updatable(self, api_instance):
        contact_info = api_instance.get_contact_info(int(self.brevoid))
        result = {

        }
        attributes = self._build_brevo_attributes_values()
        if self.email != contact_info.email:
            attributes['EMAIL'] = self.email
        result['attributes'] = attributes

        return result

    @api.model
    def sync_brevo_2_odoo(self, audience_ids=[]):
        api_instance = self.get_brevo_api_instance(
            'Contacts', self.env.company)
        limit = 50
        offset = 0
        sort = 'desc'
        list_ids = audience_ids
        params = {
            'limit': limit,
            'offset': offset,
            'sort': sort
        }
        if list_ids:
            params['list_ids'] = list_ids

        contacts = get_contats(
            api_instance=api_instance,
            **params)
        record_count = contacts.count
        self.process_brevo_to_odoo_contacts(contacts.contacts)
        if record_count:
            offset = min(offset + limit, record_count-1)
        while offset > 0 and offset < record_count-1:
            contacts = get_contats(
                api_instance=api_instance,
                **params)
            offset = min(offset + limit, record_count)
            self.process_brevo_to_odoo_contacts(contacts.contacts)
        company_api_instance = self.get_brevo_api_instance(
            'Companies', self.env.company)
        company_params = {

        }
        companies = get_contats(
            api_instance=company_api_instance,
            **company_params)
        if companies.items:
            self.process_brevo_to_odoo_contacts(
                companies.items, is_company=True)

    def _sync_odoo_2_brevo(self):
        api_instance = self.get_brevo_api_instance(
            'Contacts', self.env.company)
        for rec in self:
            if not rec.brevoid:
                contact_data = {
                    'email': rec.email,
                    'update_enabled': True,
                    'email_blacklisted': not rec.brevo_can_receive_email_campaigns,
                    'sms_blacklisted': not rec.brevo_can_receive_sms_campaigns,
                    'ext_id': str(rec.id),
                    'attributes': rec._build_brevo_attributes_values()
                }
                create_contact = brevo_python.CreateContact(**contact_data)
                try:
                    # Create a contact
                    api_response = api_instance.create_contact(create_contact)
                    resp = api_response.to_dict()
                    rec.brevoid = str(resp.get('id'))
                except ApiException as e:
                    raise UserError(
                        "Exception when calling ContactsApi->create_contact: %s\n" % e)
            else:
                identifier = int(self.brevoid)
                contact_data = {
                    'email_blacklisted': rec.is_blacklisted,
                    'sms_blacklisted':  rec.mobile_blacklisted,
                }
                try:
                    contact_data.update(
                        self._get_brevo_updatable(api_instance))
                    update_contact = brevo_python.UpdateContact(contact_data)
                    # Create a contact
                    api_response = api_instance.update_contact(
                        identifier, update_contact)
                except ApiException as e:
                    raise UserError(
                        "Exception when calling ContactsApi->create_contact: %s\n" % e)

    def _map_attributes(self, attributes, model_name=None):
        if not model_name:
            model_name = self._name
        att_ids = self.env['grev.brevo.attribute'].search(
            [('odoo_model_id.model', '=', model_name), ('brevoid', '!=', False)])
        result = {}
        for key, value in attributes.items():
            for att in att_ids:
                if att.name == key:
                    if att.odoo_map_id.name != 'tz':
                        result[att.odoo_map_id.name] = value
        return result

    def _build_brevo_attributes_values(self):
        attribute_ids = self.env['grev.brevo.attribute'].search(
            [('odoo_model_id.model', '=', self._name), ('brevoid', '!=', False)])
        res = {}
        for attr in attribute_ids:
            value = getattr(self, attr.odoo_map_id.name)
            if value:
                res[attr.name] = value
        return res

    def action_sync_odoo_2_brevo(self):
        self._sync_odoo_2_brevo()
