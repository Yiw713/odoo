from odoo import models, fields, api

class MonoRequest(models.Model):
    _name = 'mono.request'
    _description = 'Mono Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Title", required=True, tracking=True)

    employee_id = fields.Many2one(
        'hr.employee',
        string="Employee",
        default=lambda self: self.env.user.employee_id,
        required=True
    )

    request_type = fields.Selection([
        ('leave', 'Leave'),
        ('ot', 'OT'),
        ('document', 'Document'),
    ], string="Request Type", required=True, tracking=True)

    date_from = fields.Datetime("From")
    date_to = fields.Datetime("To")

    reason = fields.Text("Reason")

    attachment_ids = fields.Many2many(
        'ir.attachment',
        string="Attachments"
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('manager', 'Manager Approved'),
        ('hr', 'HR Approved'),
        ('done', 'Done'),
        ('rejected', 'Rejected'),
    ], default='draft', tracking=True)

    manager_id = fields.Many2one('res.users', string="Manager")
    hr_id = fields.Many2one('res.users', string="HR")

    # =========================
    # ACTIONS (Workflow)
    # =========================

    def action_submit(self):
        self.state = 'submitted'
        self._notify_manager()

    def action_manager_approve(self):
        self.state = 'manager'
        self._notify_hr()

    def action_hr_approve(self):
        self.state = 'hr'

    def action_done(self):
        self.state = 'done'

    def action_reject(self):
        self.state = 'rejected'

    # =========================
    # NOTIFICATION
    # =========================

    def _notify_manager(self):
        if self.manager_id:
            self.activity_schedule(
                'mail.mail_activity_data_todo',
                user_id=self.manager_id.id,
                note="Please approve request"
            )

    def _notify_hr(self):
        if self.hr_id:
            self.activity_schedule(
                'mail.mail_activity_data_todo',
                user_id=self.hr_id.id,
                note="HR Approval needed"
            )