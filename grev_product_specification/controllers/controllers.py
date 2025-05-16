# -*- coding: utf-8 -*-
# from odoo import http


# class GrevProductSpecification(http.Controller):
#     @http.route('/grev_product_specification/grev_product_specification', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grev_product_specification/grev_product_specification/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('grev_product_specification.listing', {
#             'root': '/grev_product_specification/grev_product_specification',
#             'objects': http.request.env['grev_product_specification.grev_product_specification'].search([]),
#         })

#     @http.route('/grev_product_specification/grev_product_specification/objects/<model("grev_product_specification.grev_product_specification"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grev_product_specification.object', {
#             'object': obj
#         })

