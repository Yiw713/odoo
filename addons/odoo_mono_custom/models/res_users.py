from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    mono_user_id = fields.Integer("Mono User ID")
    mono_user_name = fields.Char("Mono User Name")