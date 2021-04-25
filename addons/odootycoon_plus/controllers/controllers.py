# -*- coding: utf-8 -*-
# from odoo import http


# class OdootycoonPlus(http.Controller):
#     @http.route('/odootycoon_plus/odootycoon_plus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odootycoon_plus/odootycoon_plus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odootycoon_plus.listing', {
#             'root': '/odootycoon_plus/odootycoon_plus',
#             'objects': http.request.env['odootycoon_plus.odootycoon_plus'].search([]),
#         })

#     @http.route('/odootycoon_plus/odootycoon_plus/objects/<model("odootycoon_plus.odootycoon_plus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odootycoon_plus.object', {
#             'object': obj
#         })
