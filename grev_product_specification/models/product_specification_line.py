from odoo import models, fields, api, _


class ProductSpecificationLine(models.Model):
    _name = 'product.specification.line'
    _description = 'Product Specification Line'

    name = fields.Many2one('product.specification',
                           string='Specification', required=True)
    value = fields.Text(string='Value')
    unit_id = fields.Many2one(
        'uom.uom', string='Unit of Measure', related='name.unit_id')
    product_tmpl_id = fields.Many2one(
        'product.template', string='Product Template', ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)

    
class ProductVariantSpecificationLine(models.Model):
    _name = 'product.variant.specification.line'
    _description = 'Product Variant Specification Line'

    name = fields.Many2one('product.specification',
                           string='Specification', required=True)
    value = fields.Text(string='Value')
    unit_id = fields.Many2one(
        'uom.uom', string='Unit of Measure', related='name.unit_id')
    product_id = fields.Many2one(
        'product.product', string='Product', ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)