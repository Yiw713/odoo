# from odoo import http


# class MonoCalendar(http.Controller):
#     @http.route('/mono_calendar/mono_calendar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mono_calendar/mono_calendar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mono_calendar.listing', {
#             'root': '/mono_calendar/mono_calendar',
#             'objects': http.request.env['mono_calendar.mono_calendar'].search([]),
#         })

#     @http.route('/mono_calendar/mono_calendar/objects/<model("mono_calendar.mono_calendar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mono_calendar.object', {
#             'object': obj
#         })

