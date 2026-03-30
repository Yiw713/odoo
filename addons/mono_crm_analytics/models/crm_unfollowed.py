from odoo import models, fields, api

class CrmUnfollowed(models.Model):
    _name = 'mono.crm.unfollowed'
    _description = 'Unfollowed Leads'

    name = fields.Char()
    user_id = fields.Many2one('res.users')
    stage_id = fields.Many2one('crm.stage')

    @api.model
    def get_unfollowed(self):
        return self.env['crm.lead'].search([
            ('activity_ids', '=', False),
            ('type', '=', 'opportunity'),
            ('stage_id.is_won', '=', False)
        ])