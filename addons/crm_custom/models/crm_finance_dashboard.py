from odoo import models, fields, tools


class CrmFinanceDashboard(models.Model):
    _name = 'crm.finance.dashboard'
    _description = 'CRM Finance Dashboard'
    _auto = False

    stage_id = fields.Many2one('crm.stage', string="Stage")
    expected_revenue = fields.Float("Expected Revenue")
    total_count = fields.Integer("Opportunities")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'crm_finance_dashboard')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW crm_finance_dashboard AS (
                SELECT
                    row_number() OVER() as id,
                    stage_id,
                    SUM(expected_revenue) as expected_revenue,
                    COUNT(*) as total_count
                FROM crm_lead
                WHERE type = 'opportunity'
                GROUP BY stage_id
            )
        """)