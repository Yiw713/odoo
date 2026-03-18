# from odoo import models, fields, api


# class employee_ot_request(models.Model):
#     _name = 'employee_ot_request.employee_ot_request'
#     _description = 'employee_ot_request.employee_ot_request'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

