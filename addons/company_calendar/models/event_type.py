from odoo import models, fields

class CompanyEventType(models.Model):
    _name = "company.event.type"
    _description = "Company Event Type"

    name = fields.Char(string="Type Name", required=True)

    color = fields.Integer(string="Color")

    description = fields.Text(string="Description")