# from odoo import models, fields, api


# class odoo_mono_custom(models.Model):
#     _name = 'odoo_mono_custom.odoo_mono_custom'
#     _description = 'odoo_mono_custom.odoo_mono_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

