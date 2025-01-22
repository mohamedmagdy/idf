# -*- coding: utf-8 -*-
# from odoo import http


# class CaseManagementSystem(http.Controller):
#     @http.route('/case_management_system/case_management_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/case_management_system/case_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('case_management_system.listing', {
#             'root': '/case_management_system/case_management_system',
#             'objects': http.request.env['case_management_system.case_management_system'].search([]),
#         })

#     @http.route('/case_management_system/case_management_system/objects/<model("case_management_system.case_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('case_management_system.object', {
#             'object': obj
#         })

