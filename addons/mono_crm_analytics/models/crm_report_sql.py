from odoo import models, fields, tools

class CrmReport(models.Model):
    _name = 'mono.crm.report.sql'
    _description = 'CRM Analytics SQL'
    _auto = False

    create_date = fields.Date()
    user_id = fields.Many2one('res.users', string="Sales")
    team_id = fields.Many2one('crm.team', string="Team")

    total_leads = fields.Integer()
    total_won = fields.Integer()
    total_lost = fields.Integer()
    expected_revenue = fields.Float()

    conversion_rate = fields.Float(compute="_compute_conversion")

    def _compute_conversion(self):
        for rec in self:
            rec.conversion_rate = (rec.total_won / rec.total_leads * 100) if rec.total_leads else 0

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
        CREATE OR REPLACE VIEW mono_crm_report_sql AS (
            SELECT
                MIN(l.id) as id,
                DATE(l.create_date) as create_date,
                l.user_id,
                l.team_id,

                COUNT(*) as total_leads,

                SUM(CASE WHEN s.is_won THEN 1 ELSE 0 END) as total_won,

                SUM(CASE 
                    WHEN s.is_won = false AND l.probability = 0 
                    THEN 1 ELSE 0 
                END) as total_lost,

                SUM(l.expected_revenue) as expected_revenue

            FROM crm_lead l
            LEFT JOIN crm_stage s ON l.stage_id = s.id
            WHERE l.type = 'opportunity'
            GROUP BY DATE(l.create_date), l.user_id, l.team_id
        )
    """)