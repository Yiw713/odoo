from odoo import models, fields, tools


class MonoDashboard(models.Model):
    _name = 'mono.dashboard'
    _description = 'Mono Dashboard'
    _auto = False

    vehicle_id = fields.Char()
    total_records = fields.Integer()
    avg_speed = fields.Float()

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'mono_dashboard')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW mono_dashboard AS (
                SELECT
                    row_number() OVER() as id,
                    vehicle_id,
                    COUNT(*) as total_records,
                    AVG(speed) as avg_speed
                FROM mono_api_data
                GROUP BY vehicle_id
            )
        """)