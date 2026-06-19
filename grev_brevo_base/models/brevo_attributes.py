import logging
import brevo_python
from brevo_python.rest import ApiException
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class BrevoAttributes(models.Model):
    _name = 'grev.brevo.attribute'
    _inherit = ['grev.brevo.mixin']
    _description = 'Brevo attribute'

    brevoid = fields.Char(default="synced")
    name = fields.Char(required=True)
    odoo_map_id = fields.Many2one(
        'ir.model.fields', ondelete='cascade', required=True)
    odoo_model_id = fields.Many2one(
        'ir.model',
        ondelete='cascade', 
        required=True,
        default=lambda self:self.env.ref('base.model_res_partner')
        )

    @api.model
    def process_brevo_to_odoo_attributes(self, attributes):
        odoo_attributes = {}
        for attribute in attributes:
            pass

    @api.model
    def sync_brevo_2_odoo(self):
        api_instance = self.get_brevo_api_instance(
            'Contacts', self.env.company)
        attributes = api_instance.get_attributes()

        self.process_brevo_to_odoo_attributes(attributes)

    def _sync_odoo_2_brevo(self):
        api_instance = self.get_brevo_api_instance(
            'Contacts', self.env.company)
        for rec in self:
            if not rec.brevoid:
                attribute_data = {
                    'type': 'text'
                }
                # ['text', 'date', 'float', 'boolean', 'id', 'category', 'multiple-choice']
                create_attribute = brevo_python.CreateAttribute(
                    **attribute_data)
                try:
                    # Create a attribute
                    attribute_category = 'normal'
                    attribute_name = rec.name
                    api_response = api_instance.create_attribute(
                        attribute_category, attribute_name, create_attribute)
                    rec.brevoid = 'synced'
                except ApiException as e:
                    _logger.info(
                        "Exception when calling AttributesApi->create_attribute: %s\n" % e)
            else:

                attribute_data = {

                }
                update_attribute = brevo_python.UpdateAttribute(attribute_data)
                try:
                    attribute_category = 'normal'
                    attribute_name = rec.name
                    api_response = api_instance.update_attribute(
                        attribute_category, attribute_name, update_attribute)
                except ApiException as e:
                    _logger.info(
                        "Exception when calling AttributesApi->update_attribute: %s\n" % e)

    def action_sync_odoo_2_brevo(self):
        self._sync_odoo_2_brevo()
