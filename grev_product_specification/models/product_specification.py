from odoo import models, fields, api, _


class ProductSpecificationLine(models.Model):
    _name = 'product.specification'
    _description = 'Product Specification'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    unit_id = fields.Many2one('uom.uom', string='Unit of Measure', required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.code}] {record.name}"
            result.append((record.id, name))
        return result
