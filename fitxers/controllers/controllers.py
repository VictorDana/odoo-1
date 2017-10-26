# -*- coding: utf-8 -*-
from odoo import http

# class Fitxers(http.Controller):
#     @http.route('/fitxers/fitxers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fitxers/fitxers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fitxers.listing', {
#             'root': '/fitxers/fitxers',
#             'objects': http.request.env['fitxers.fitxers'].search([]),
#         })

#     @http.route('/fitxers/fitxers/objects/<model("fitxers.fitxers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fitxers.object', {
#             'object': obj
#         })