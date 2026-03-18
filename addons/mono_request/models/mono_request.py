from odoo import models, fields, api

class MonoRequest(models.Model):
    _inherit = 'project.task'

    request_no = fields.Char(
        string="Request No",
        readonly=True,
        copy=False
    )

    request_type = fields.Selection([
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('support', 'Support'),
        ('other', 'Other')
    ], string="Request Type")

    requester_id = fields.Many2one(
        'res.users',
        string="Requester",
        default=lambda self: self.env.user
    )

    responsible_id = fields.Many2one(
        'res.users',
        string="Responsible"
    )

    priority_level = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Critical')
    ], default='0')

    image = fields.Binary("Image")

    request_state = fields.Selection([
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
    ('approved', 'Approved'),
    ('progress', 'In Progress'),
    ('done', 'Done'),
    ('cancel', 'Cancelled')
], default='draft', tracking=True)

    approve_user = fields.Many2one('res.users')
    approve_date = fields.Datetime()

    @api.model
    def create(self, vals):
        if not vals.get('request_no'):
            vals['request_no'] = self.env['ir.sequence'].next_by_code('mono.request')
        return super(MonoRequest, self).create(vals)

    def action_submit(self):
        self.request_state = 'submitted'

    def action_approve(self):
        self.request_state = 'approved'
        self.approve_user = self.env.user
        self.approve_date = fields.Datetime.now()

    def action_progress(self):
        self.request_state = 'progress'

    def action_done(self):
        self.request_state = 'done'