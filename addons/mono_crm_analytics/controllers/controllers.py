# from odoo import http


# class MonoCrmAnalytics(http.Controller):
#     @http.route('/mono_crm_analytics/mono_crm_analytics', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mono_crm_analytics/mono_crm_analytics/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mono_crm_analytics.listing', {
#             'root': '/mono_crm_analytics/mono_crm_analytics',
#             'objects': http.request.env['mono_crm_analytics.mono_crm_analytics'].search([]),
#         })

#     @http.route('/mono_crm_analytics/mono_crm_analytics/objects/<model("mono_crm_analytics.mono_crm_analytics"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mono_crm_analytics.object', {
#             'object': obj
#         })

