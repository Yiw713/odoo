from odoo import models, fields, api
import requests

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    lead_source = fields.Char(string="Lead Source")

    product_type = fields.Selection([
        ('gps', 'GPS'),
        ('mdvr', 'MDVR'),
        ('gps_mdvr', 'GPS+MDVR'),
        ('rack_tracking', 'Rack tracking'),
        ('forklift_solution', 'Forklift Solution'),
        ('dlt', 'DLT'),
        ('iot', 'IoT'),
        ('marine_solution', 'Marine Solution')
    ], string="Product Type")

    lead_note = fields.Text(string="Note")

    tax_id = fields.Char(string="Tax ID", size=13)

    priority = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ], string="Priority", default='0')

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