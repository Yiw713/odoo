from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    mono_state = fields.Selection([
        ('draft', 'Draft'),
        ('pending_approval', 'Pending Approval'),
        ('reviewing', 'Reviewing'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('pending_review', 'Pending Review'),
        ('qa_review', 'QA Review'),
        ('pending_acceptance', 'Pending Acceptance'),
        ('done', 'Done'),
    ], default='draft', tracking=True)

    progress = fields.Integer(default=0)
    revision_count = fields.Integer(default=0)

    deadline = fields.Datetime()
    finished_date = fields.Datetime()

    delay_days = fields.Integer(compute="_compute_delay", store=True)
    deadline_extend_count = fields.Integer(default=0)

    # -----------------------
    @api.depends('deadline', 'finished_date')
    def _compute_delay(self):
        for rec in self:
            if rec.deadline and rec.finished_date:
                rec.delay_days = int((rec.finished_date - rec.deadline).total_seconds() / 86400)
            else:
                rec.delay_days = 0

    # -----------------------
    def _update_stage_from_state(self):
        self.ensure_one()

        stage = self.env['project.task.type'].search([
            ('stage_code', '=', self.mono_state),
            ('mono_type', '=', self.project_id.mono_type),
            ('project_ids', 'in', self.project_id.id)  # 👈 สำคัญ
        ], limit=1)

        if stage:
            self.with_context(from_mono=True).stage_id = stage.id

    # -----------------------
    def _update_state_from_stage(self):
        self.ensure_one()

        if self.stage_id.stage_code:
            self.mono_state = self.stage_id.stage_code

    # -----------------------
    def write(self, vals):
        if 'deadline' in vals:
            for rec in self:
                if rec.deadline:
                    rec.deadline_extend_count += 1

        res = super().write(vals)

        if 'mono_state' in vals:
            for rec in self:
                rec._update_stage_from_state()

        if 'stage_id' in vals and not self.env.context.get('from_mono'):
            for rec in self:
                rec._update_state_from_stage()

        return res

    # -----------------------
    @api.model
    def create(self, vals):
        task = super().create(vals)
        task._update_stage_from_state()
        return task

    # -----------------------
    # Workflow
    # -----------------------
    def action_submit(self):
        self.mono_state = 'pending_approval'

    def action_approve(self):
        if self.project_id.mono_type == 'outsource':
            self.mono_state = 'reviewing'
        else:
            self.mono_state = 'assigned'

    def action_start(self):
        self.mono_state = 'in_progress'

    def action_submit_review(self):
        if self.project_id.mono_type == 'outsource':
            self.mono_state = 'pending_review'
        else:
            self.mono_state = 'qa_review'

    def action_qa_pass(self):
        self.mono_state = 'pending_acceptance'

    def action_qa_fail(self):
        self.revision_count += 1
        self.mono_state = 'in_progress'

    def action_accept(self):
        self.mono_state = 'done'
        self.finished_date = fields.Datetime.now()
