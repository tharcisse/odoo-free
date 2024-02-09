from odoo import models, fields, api


class ShareType(models.Model):
    _name = 'res.company.share.type'
    _description = 'Company Share type'

    name = fields.Char()
    code = fields.Char()
    token = fields.Many2one('crypto.token')
    blochained = fields.Boolean()
    blockchain_id = fields.Many2one('crypto.blockchain')


class LegalDocumentType(models.Model):
    _name = 'res.company.legal.document.type'
    _description = 'Legal Document Type'

    name = fields.Char()


class Legaldocument(models.Model):
    _name = 'res.company.legal.document'
    _description = 'Company Legal Documents'

    name = fields.Char(required="1")
    type_id = fields.Many2one('res.company.legal.document.type', required=1)
    document_id = fields.Many2one('ir.attachment')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)
    document_date = fields.Date(required=1)
    oj_registratrion_number = fields.Char('OJ Reg Number')


class StakeHolders(models.Model):
    _name = 'res.company.shareholder'
    _description = 'Company Stakeholder'

    partner_id = fields.Many2one('res.partner', 'Share holder')
    num_of_shares = fields.Integer('# of Shares')
    type_id = fields.Many2one('res.company.share.type')
    par_value = fields.Monetary()
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company')
