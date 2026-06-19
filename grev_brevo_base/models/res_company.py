import time
import inspect
import logging
import brevo_python
from brevo_python.rest import ApiException

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class Company(models.Model):
    _inherit = 'res.company'

    brevo_api_key = fields.Char()
    is_brevo_supported = fields.Boolean(compute='_compute_is_brevo_supported')

    @api.depends('brevo_api_key')
    def _compute_is_brevo_supported(self):
        for rec in self:
            rec.is_brevo_supported = bool(rec.brevo_api_key)

    def _get_brevo_api_instance(self, type='Account'):
        configuration = brevo_python.Configuration()
        configuration.api_key['api-key'] = self.brevo_api_key
        api_client = brevo_python.ApiClient(configuration)
        api_instance = None
        matching_api_class = [
            obj for name, obj in inspect.getmembers(brevo_python, inspect.isclass)
            if name == type+'Api']
        if matching_api_class:
            api_instance = matching_api_class[0](api_client)

        return api_instance
