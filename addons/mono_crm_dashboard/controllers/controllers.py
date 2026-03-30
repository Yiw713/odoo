# from odoo import http


# class MonoCrmDashboard(http.Controller):
#     @http.route('/mono_crm_dashboard/mono_crm_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mono_crm_dashboard/mono_crm_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mono_crm_dashboard.listing', {
#             'root': '/mono_crm_dashboard/mono_crm_dashboard',
#             'objects': http.request.env['mono_crm_dashboard.mono_crm_dashboard'].search([]),
#         })

#     @http.route('/mono_crm_dashboard/mono_crm_dashboard/objects/<model("mono_crm_dashboard.mono_crm_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mono_crm_dashboard.object', {
#             'object': obj
#         })

