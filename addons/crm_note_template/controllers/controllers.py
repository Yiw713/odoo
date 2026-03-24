# from odoo import http


# class CrmNoteTemplate(http.Controller):
#     @http.route('/crm_note_template/crm_note_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_note_template/crm_note_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_note_template.listing', {
#             'root': '/crm_note_template/crm_note_template',
#             'objects': http.request.env['crm_note_template.crm_note_template'].search([]),
#         })

#     @http.route('/crm_note_template/crm_note_template/objects/<model("crm_note_template.crm_note_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_note_template.object', {
#             'object': obj
#         })

