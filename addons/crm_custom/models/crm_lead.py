from odoo import models, fields, api
import requests


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_customer_budget = fields.Float(string="Customer Budget")
    x_project_deadline = fields.Date(string="Project Deadline")

    x_api_status = fields.Char("API Status")
    x_log_count = fields.Integer(
        string="Log Count",
        compute="_compute_log_count"
    )

    def _compute_log_count(self):
        for rec in self:
            rec.x_log_count = self.env['crm.custom.log'].search_count([
                ('lead_id', '=', rec.id)
            ])

    def action_view_logs(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Logs',
            'res_model': 'crm.custom.log',
            'view_mode': 'list,form',
            'domain': [('lead_id', '=', self.id)],
            'context': {'default_lead_id': self.id},
        }
