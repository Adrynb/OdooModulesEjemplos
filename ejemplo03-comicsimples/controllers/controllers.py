# -*- coding: utf-8 -*-
# from odoo import http


# class Comicsimples(http.Controller):
#     @http.route('/comicsimples/comicsimples', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comicsimples/comicsimples/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comicsimples.listing', {
#             'root': '/comicsimples/comicsimples',
#             'objects': http.request.env['comicsimples.comicsimples'].search([]),
#         })

#     @http.route('/comicsimples/comicsimples/objects/<model("comicsimples.comicsimples"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comicsimples.object', {
#             'object': obj
#         })

