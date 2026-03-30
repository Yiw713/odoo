from odoo import models, fields, tools

class CrmActivity(models.Model):
    _name = 'mono.crm.activity.sql'
    _description = 'CRM Activity SQL'
    _auto = False

    user_id = fields.Many2one('res.users')
    total_calls = fields.Integer()
    total_meetings = fields.Integer()

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW mono_crm_activity_sql AS (
                SELECT
                    MIN(a.id) as id,
                    a.user_id,

                    COUNT(*) FILTER (WHERE a.activity_type_id = 1) as total_calls,
                    COUNT(*) FILTER (WHERE a.activity_type_id = 2) as total_meetings

                FROM mail_activity a
                WHERE a.res_model = 'crm.lead'
                GROUP BY a.user_id
            )
        """)