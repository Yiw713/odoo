# from odoo import http


# class MonoCrmReport(http.Controller):
#     @http.route('/mono_crm_report/mono_crm_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mono_crm_report/mono_crm_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mono_crm_report.listing', {
#             'root': '/mono_crm_report/mono_crm_report',
#             'objects': http.request.env['mono_crm_report.mono_crm_report'].search([]),
#         })

#     @http.route('/mono_crm_report/mono_crm_report/objects/<model("mono_crm_report.mono_crm_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mono_crm_report.object', {
#             'object': obj
#         })

