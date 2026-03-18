# from odoo import http


# class RequestMono(http.Controller):
#     @http.route('/request_mono/request_mono', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/request_mono/request_mono/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('request_mono.listing', {
#             'root': '/request_mono/request_mono',
#             'objects': http.request.env['request_mono.request_mono'].search([]),
#         })

#     @http.route('/request_mono/request_mono/objects/<model("request_mono.request_mono"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('request_mono.object', {
#             'object': obj
#         })

