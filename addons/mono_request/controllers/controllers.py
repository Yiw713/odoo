# from odoo import http


# class MonoRequest(http.Controller):
#     @http.route('/mono_request/mono_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mono_request/mono_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mono_request.listing', {
#             'root': '/mono_request/mono_request',
#             'objects': http.request.env['mono_request.mono_request'].search([]),
#         })

#     @http.route('/mono_request/mono_request/objects/<model("mono_request.mono_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mono_request.object', {
#             'object': obj
#         })

