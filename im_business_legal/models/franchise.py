from odoo import models, fields, api, _


class FranchiseModel(models.Model):
    _name = 'im.legal.franchise.model'
    _description = 'Franchise Model'

    name = fields.Char(required=True)
    description = fields.Text()
    code = fields.Char(required=True)


class FranchiseOperatingModel(models.Model):
    _name = 'im.legal.franshise.operating.model'
    _description = 'Franchise Operating Model'

    name = fields.Char(required=True)
    code = fields.Char('required=True')
    description = fields.Text()
