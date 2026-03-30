# from odoo import models, fields, api


# class mono_crm_dashboard(models.Model):
#     _name = 'mono_crm_dashboard.mono_crm_dashboard'
#     _description = 'mono_crm_dashboard.mono_crm_dashboard'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

