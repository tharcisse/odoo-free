from odoo import models, fields, api


class Shareholders(models.Model):
    _name = 'res.company.shareholder'
    _description = 'Shareholders'

    partner_id = fields.Many2one('res.partner')
    shares = fields.Integer()
    ratio = fields.Float()
    complete_name = fields.Char(compute='_compute_complete_name', store=True)
    company_id = fields.Many2one()

    @api.depends('partner_id', 'partner_id.name', 'shares', 'ratio')
    def _compute_complete_name(self):
        for rec in self:
            value = ''
            if rec.partner_id and rec.partner_id.name:
                value = rec.partner_id.name
            if rec.ratio:
                value += f'({rec.ratio} %'
            rec.complete_name = value
    
