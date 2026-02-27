# from odoo import http


# class OdooMonoCustom(http.Controller):
#     @http.route('/odoo_mono_custom/odoo_mono_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_mono_custom/odoo_mono_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_mono_custom.listing', {
#             'root': '/odoo_mono_custom/odoo_mono_custom',
#             'objects': http.request.env['odoo_mono_custom.odoo_mono_custom'].search([]),
#         })

#     @http.route('/odoo_mono_custom/odoo_mono_custom/objects/<model("odoo_mono_custom.odoo_mono_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_mono_custom.object', {
#             'object': obj
#         })

