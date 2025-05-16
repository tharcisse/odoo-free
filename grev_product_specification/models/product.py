from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    specification_ids = fields.One2many(
        'product.specification.line', 'product_tmpl_id', string='Specifications')
    specification_count = fields.Integer(
        string='Specification Count', compute='_compute_specification_count')

    @api.depends('specification_ids')
    def _compute_specification_count(self):
        for record in self:
            record.specification_count = len(record.specification_ids)

    def build_specification_from_category(self):
        for record in self:
            if record.categ_id and record.categ_id.specification_ids:
                for spec in record.categ_id.specification_ids:
                    self.env['product.specification.line'].create({
                        'name': spec.id,
                        'product_tmpl_id': record.id,
                        'value': False,
                        'unit': spec.unit.id,
                        'sequence': spec.sequence,
                    })

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.build_specification_from_category()
        return records


class ProductProduct(models.Model):
    _inherit = 'product.product'

    variant_specification_ids = fields.One2many(
        'product.variant.specification.line', 'product_id', string='Specifications')
    variant_specification_count = fields.Integer(
        string='Variant Specification Count', compute='_compute_specification_count')

    @api.depends('specification_ids')
    def _compute_specification_count(self):
        for record in self:
            record.variant_specification_count = len(record.variant_specification_ids)

    def build_specification_from_product_template(self):
        for record in self:
            if record.product_tmpl_id and record.product_tmpl_id.specification_ids:
                for spec in record.product_tmpl_id.specification_ids:
                    self.env['product.variant.specification.line'].create({
                        'name': spec.id,
                        'product_id': record.id,
                        'value': spec.value,
                        'unit': spec.unit.id,
                        'sequence': spec.sequence,
                    })

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.build_specification_from_product_template()
        return records
