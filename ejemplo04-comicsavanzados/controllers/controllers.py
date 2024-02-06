# -*- coding: utf-8 -*-
# from odoo import http


# class Comicsavanzados(http.Controller):
#     @http.route('/comicsavanzados/comicsavanzados', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comicsavanzados/comicsavanzados/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comicsavanzados.listing', {
#             'root': '/comicsavanzados/comicsavanzados',
#             'objects': http.request.env['comicsavanzados.comicsavanzados'].search([]),
#         })

#     @http.route('/comicsavanzados/comicsavanzados/objects/<model("comicsavanzados.comicsavanzados"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comicsavanzados.object', {
#             'object': obj
#         })

