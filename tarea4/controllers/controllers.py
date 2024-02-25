# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea4(http.Controller):
#     @http.route('/tarea4/tarea4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea4/tarea4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea4.listing', {
#             'root': '/tarea4/tarea4',
#             'objects': http.request.env['tarea4.tarea4'].search([]),
#         })

#     @http.route('/tarea4/tarea4/objects/<model("tarea4.tarea4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea4.object', {
#             'object': obj
#         })

