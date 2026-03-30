from odoo import models, fields, api

class CrmReport(models.TransientModel):
    _name = 'mono.crm.report'
    _description = 'CRM Summary Report'

    date_from = fields.Date(string="From Date")
    date_to = fields.Date(string="To Date")

    total_leads = fields.Integer(string="Total Leads", readonly=True)
    total_won = fields.Integer(string="Total Won", readonly=True)
    total_activities = fields.Integer(string="Total Activities", readonly=True)

    def action_generate_report(self):
        self.ensure_one()

        domain = [
            ('create_date', '>=', self.date_from),
            ('create_date', '<=', self.date_to)
        ]

        # 1. ลูกค้าใหม่
        leads = self.env['crm.lead'].search(domain)
        self.total_leads = len(leads)

        # 2. ปิดการขาย (stage = won)
        won_leads = self.env['crm.lead'].search(domain + [('stage_id.is_won', '=', True)])
        self.total_won = len(won_leads)

        # 3. การติดต่อลูกค้า
        activities = self.env['mail.activity'].search([
            ('create_date', '>=', self.date_from),
            ('create_date', '<=', self.date_to),
            ('res_model', '=', 'crm.lead')
        ])
        self.total_activities = len(activities)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mono.crm.report',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }