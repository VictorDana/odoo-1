# -*- coding: utf-8 -*-
from odoo import http

# class Modul2(http.Controller):
#     @http.route('/modul2/modul2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modul2/modul2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modul2.listing', {
#             'root': '/modul2/modul2',
#             'objects': http.request.env['modul2.modul2'].search([]),
#         })

#     @http.route('/modul2/modul2/objects/<model("modul2.modul2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modul2.object', {
#             'object': obj
#         })