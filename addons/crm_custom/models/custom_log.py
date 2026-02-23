from odoo import models, fields

class CrmCustomLog(models.Model):
    _name = 'crm.custom.log'
    _description = 'CRM Custom Log'

    name = fields.Char("Description")
    lead_id = fields.Many2one('crm.lead', string="Lead")
