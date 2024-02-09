from odoo import models, fields, api, _


class Classification(models.Model):
    _name = 'res.company.classification'
    _description = 'ISIC Company classification'

    nam = fields.Char()
    code = fields.Char()


class BusinessModel(models.Model):
    _name = 'res.business.model'
    _description = 'Business Model'

    name = fields.Char()
    code = fields.Char()


class Company(models.Model):
    _inherit = 'res.company'

    legal_name = fields.Char()
    legal_structure_id = fields.Many2one('res.company.legal.structure')
    description = fields.Text()
    classification_ids = fields.Many2many('res.company.classification',
                                          relation='res_company_classifiacation_rel', string='Classification')
    date_formation = fields.Date()
    founder_ids = fields.Many2many('res.partner', relation='res_company_founders_rel', string='Founders')
    shareholder_ids = fields.One2many('res.company.shareholder', 'company_id')
    legal_document_ids = fields.One2many('res.company.legal.document', 'company_id')
    business_model = fields.Many2one('res.business.model')
