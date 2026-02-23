from odoo import models, fields, tools


class CrmFollowupDashboard(models.Model):
    _name = 'crm.followup.dashboard'
    _description = 'CRM Followup Dashboard'
    _auto = False  # บอกว่าไม่สร้าง table ปกติ เพราะใช้ SQL view

    user_id = fields.Many2one('res.users', string="User")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('overdue', 'Overdue')
    ])
    total = fields.Integer("Total")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'crm_followup_dashboard')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW crm_followup_dashboard AS (
                SELECT
                    row_number() OVER() as id,
                    user_id,
                    status,
                    COUNT(*) as total
                FROM crm_followup
                GROUP BY user_id, status
            )
        """)
