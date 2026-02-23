from odoo import models, fields


class CrmFollowup(models.Model):
    _name = 'crm.followup'
    _description = 'CRM Follow Up'

    name = fields.Char("Subject", required=True)
    lead_id = fields.Many2one('crm.lead', string="Lead")
    user_id = fields.Many2one('res.users', string="Assigned To")
    followup_date = fields.Datetime("Follow Up Date")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('overdue', 'Overdue')
    ], default='pending')
