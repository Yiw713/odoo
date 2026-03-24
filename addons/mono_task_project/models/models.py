# from odoo import models, fields, api


# class mono_task_project(models.Model):
#     _name = 'mono_task_project.mono_task_project'
#     _description = 'mono_task_project.mono_task_project'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

