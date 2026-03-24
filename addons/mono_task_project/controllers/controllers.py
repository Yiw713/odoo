# from odoo import http


# class MonoTaskProject(http.Controller):
#     @http.route('/mono_task_project/mono_task_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mono_task_project/mono_task_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mono_task_project.listing', {
#             'root': '/mono_task_project/mono_task_project',
#             'objects': http.request.env['mono_task_project.mono_task_project'].search([]),
#         })

#     @http.route('/mono_task_project/mono_task_project/objects/<model("mono_task_project.mono_task_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mono_task_project.object', {
#             'object': obj
#         })

