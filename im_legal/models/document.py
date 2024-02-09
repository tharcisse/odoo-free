from odoo import models, fields, api, _


class LegalDocumentType(models.Model):
    _name = 'im.legal.document.type'
    _description = 'Legal Document Type'

    name = fields.Char()
    code = fields.Char(required=True)


class Legaldocument(models.Model):
    _name = 'im.legal.document'
    _description = 'Company Legal Documents'

    name = fields.Char(required=True)
    type_id = fields.Many2one('im.legal.document.type', required=1)
    document_id = fields.Many2one('ir.attachment')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    document_date = fields.Date(required=1,default=fields.Date.today())
    oj_registration_number = fields.Char('OJ Reg Number')
