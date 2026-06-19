from odoo import models, fields, api


class ConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_brevo_api_key = fields.Char(
        related='company_id.brevo_api_key', readonly=False)
    auto_update_brevo_contacts = fields.Boolean(
        config_param='auto_update_brevo_contacts')

    
    
