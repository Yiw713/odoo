# from odoo import http


# class CompanyCalender(http.Controller):
#     @http.route('/company_calender/company_calender', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_calender/company_calender/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_calender.listing', {
#             'root': '/company_calender/company_calender',
#             'objects': http.request.env['company_calender.company_calender'].search([]),
#         })

#     @http.route('/company_calender/company_calender/objects/<model("company_calender.company_calender"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_calender.object', {
#             'object': obj
#         })

