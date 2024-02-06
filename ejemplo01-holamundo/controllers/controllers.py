# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo01-holamundo(http.Controller):
#     @http.route('/ejemplo01-holamundo/ejemplo01-holamundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo01-holamundo/ejemplo01-holamundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo01-holamundo.listing', {
#             'root': '/ejemplo01-holamundo/ejemplo01-holamundo',
#             'objects': http.request.env['ejemplo01-holamundo.ejemplo01-holamundo'].search([]),
#         })

#     @http.route('/ejemplo01-holamundo/ejemplo01-holamundo/objects/<model("ejemplo01-holamundo.ejemplo01-holamundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo01-holamundo.object', {
#             'object': obj
#         })

