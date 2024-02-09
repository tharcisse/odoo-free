from odoo import models, fields, api


class ShareType(models.Model):
    _name = 'im.legal.share.type'
    _description = 'Company Share type'

    name = fields.Char()
    code = fields.Char()
    # token = fields.Many2one('crypto.token')
    blockchained = fields.Boolean()
    company_id = fields.Many2one('res.company', required=True,default=lambda self:self.env.company)


class StakeHolders(models.Model):
    _name = 'im.legal.shareholder'
    _description = 'Company Stakeholder'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', 'Share holder')
    num_of_shares = fields.Integer('# of Shares')
    type_id = fields.Many2one('im.legal.share.type', 'Share type')
    start_date = fields.Date(required=True, default=fields.Date.today())
    company_id = fields.Many2one('res.company',default=lambda self:self.env.company)
