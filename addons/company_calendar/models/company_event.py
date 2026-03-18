from odoo import models, fields

class CompanyEvent(models.Model):
    _name = "company.event"
    _description = "Company Event"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Event Name", required=True)

    event_type_id = fields.Many2one(
        "company.event.type",
        string="Event Type"
    )

    start_date = fields.Datetime(
        string="Start Date",
        required=True
    )

    end_date = fields.Datetime(
        string="End Date"
    )

    all_day = fields.Boolean(
        string="All Day",
        default=True
    )

    description = fields.Text(
        string="Description"
    )

    color = fields.Integer(
        related="event_type_id.color",
        store=True
    )