# from odoo import http


# class EmployeeOtRequest(http.Controller):
#     @http.route('/employee_ot_request/employee_ot_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_ot_request/employee_ot_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_ot_request.listing', {
#             'root': '/employee_ot_request/employee_ot_request',
#             'objects': http.request.env['employee_ot_request.employee_ot_request'].search([]),
#         })

#     @http.route('/employee_ot_request/employee_ot_request/objects/<model("employee_ot_request.employee_ot_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_ot_request.object', {
#             'object': obj
#         })

