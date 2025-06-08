import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class BrevoMixin(models.AbstractModel):
    _name = 'grev.brevo.mixin'
    _description = 'Brevo mixin'

    @api.model
    def get_brevo_api_instance(self, api_name, company_id):
        api_instance = company_id._get_brevo_api_instance(api_name)
        return api_instance

 

    
