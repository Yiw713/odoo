from odoo import models, fields


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    mono_event_type = fields.Selection([
        ('holiday', 'Company Holiday'),
        ('event', 'Company Event'),
        ('activity', 'Company Activity')
    ], string="Mono Event Type")

    is_mono_event = fields.Boolean(
        string="Mono Calendar Event",
        default=False
    )