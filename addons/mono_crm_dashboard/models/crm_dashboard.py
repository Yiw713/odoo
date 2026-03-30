from odoo import models, api

class CrmDashboard(models.Model):
    _name = 'crm.dashboard'
    _description = 'CRM Dashboard'

    @api.model
    def get_all(self, **kwargs):
        # ================= KPI =================
        leads = self.env['crm.lead']

        total = leads.search_count([])
        won = leads.search_count([('stage_id.is_won', '=', True)])
        conversion = (won / total * 100) if total else 0

        # ================= CHART =================
        self.env.cr.execute("""
            SELECT 
                DATE(create_date) as date,
                COUNT(*) as total,
                SUM(CASE WHEN stage_id IN (
                    SELECT id FROM crm_stage WHERE is_won = true
                ) THEN 1 ELSE 0 END) as won
            FROM crm_lead
            GROUP BY DATE(create_date)
            ORDER BY date
        """)
        chart = self.env.cr.dictfetchall()

        # ================= ACTIVITY (FIXED) =================
        self.env.cr.execute("""
            SELECT 
                u.id,
                p.name,
                COUNT(a.id) as count
            FROM mail_activity a
            JOIN res_users u ON a.user_id = u.id
            JOIN res_partner p ON u.partner_id = p.id
            GROUP BY u.id, p.name
            ORDER BY count DESC
        """)
        activity = self.env.cr.dictfetchall()

        # ================= FUNNEL =================
        self.env.cr.execute("""
            SELECT 
                s.id,
                s.name,
                COUNT(l.id) as count
            FROM crm_lead l
            JOIN crm_stage s ON l.stage_id = s.id
            GROUP BY s.id, s.name, s.sequence
            ORDER BY s.sequence
        """)
        funnel = self.env.cr.dictfetchall()

        return {
            'kpi': {
                'total': total,
                'won': won,
                'conversion': round(conversion, 2),
            },
            'chart': chart,
            'activity': activity,
            'funnel': funnel,
        }