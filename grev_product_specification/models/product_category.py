from odoo import models, fields, api, _

class ProductCategory(models.Model):
    _inherit = 'product.category'

    specification_ids = fields.Many2many(
        'product.specification', relation='product_category_specification_rel', string='Specifications')
    specification_count = fields.Integer(
        string='Specification Count', compute='_compute_specification_count')

    @api.depends('specification_ids')
    def _compute_specification_count(self):
        for record in self:
            record.specification_count = len(record.specification_ids)