# -*- coding: utf-8 -*-
# from odoo import http


# class Listatareascalender(http.Controller):
#     @http.route('/listatareascalender/listatareascalender', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/listatareascalender/listatareascalender/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('listatareascalender.listing', {
#             'root': '/listatareascalender/listatareascalender',
#             'objects': http.request.env['listatareascalender.listatareascalender'].search([]),
#         })

#     @http.route('/listatareascalender/listatareascalender/objects/<model("listatareascalender.listatareascalender"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('listatareascalender.object', {
#             'object': obj
#         })

