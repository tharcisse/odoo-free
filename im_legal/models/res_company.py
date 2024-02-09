from odoo import models, fields, api, _


class LegalStructure(models.Model):
    _name = 'im.legal.structure'
    _description = 'Legal Structure'

    name = fields.Char()
    code = fields.Char()


class Classificationsection(models.Model):
    _name = 'im.legal.classification.section'
    _description = 'ISIC Company Section'

    name = fields.Char()
    code = fields.Char()


class ClassificationDivision(models.Model):
    _name = 'im.legal.classification.division'
    _description = 'ISIC Company Division'

    name = fields.Char()
    code = fields.Char()
    section_id = fields.Many2one('im.legal.classification.section',required=True)


class ClassificationGroup(models.Model):
    _name = 'im.legal.classification.group'
    _description = 'ISIC Company group'

    name = fields.Char()
    code = fields.Char()
    division_id = fields.Many2one('im.legal.classification.division',required=True)


class Classification(models.Model):
    _name = 'im.legal.classification'
    _description = 'ISIC Company classification'

    name = fields.Char()
    code = fields.Char()
    group_id = fields.Many2one('im.legal.classification.group', required=True)
    division_id = fields.Many2one('im.legal.classification.division',related="group_id.division_id",store=True)
    section_id = fields.Many2one('im.legal.classification.section',related="group_id.division_id.section_id",store=True)


class BusinessModel(models.Model):
    _name = 'res.business.model'
    _description = 'Business Model'

    name = fields.Char()
    code = fields.Char(required=True)


class Company(models.Model):
    _inherit = 'res.company'

    legal_name = fields.Char()
    legal_structure_id = fields.Many2one('im.legal.structure')
    description = fields.Text()
    classification_ids = fields.Many2many('im.legal.classification',
                                          relation='im_legal_classifiacation_rel', string='Classification',required=True)
    date_formation = fields.Date(default=fields.Date.today())
    founder_ids = fields.Many2many('res.partner', relation='res_company_founders_rel', string='Founders')
    shareholder_ids = fields.One2many('im.legal.shareholder', 'company_id')
    legal_document_ids = fields.One2many('im.legal.document', 'company_id')
    business_model = fields.Many2one('res.business.model')
    par_value = fields.Monetary()
    total_share = fields.Integer()
