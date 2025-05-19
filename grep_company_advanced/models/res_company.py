from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    description = fields.Text()
    legal_classification = fields.Selection([
        ('llc', 'Limited Liability'),
        ('holding', 'Holding Company'),
        ('partnership', 'Partnership'),
        ('associate', 'Associate Company'),
        ('inc', 'For Profit Corporation'),
        ('sole', 'Sole Proprietorship'),
        ('public', 'Public Company'),
        ('subsidiary', 'Subsidiary'),
        ('internal_spinoff', 'Internal Spinoff')
    ])
    industry_id = fields.Many2one(
        'res.partner.industry',
        related='partner_id.industry_id',
        store=True,
        readonly=False
    )

    license_number = fields.Char('Lic. Number')
    license_valid_until = fields.Date('Lic. valid Until')
    total_shares = fields.Integer()
    shareholder_ids = fields.One2many('res.coompany.shareholder',
                                       'company_id',
                                       string='Shareholders')
