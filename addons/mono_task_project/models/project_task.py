from odoo import models, fields, api

MONO_STAGE_MAP = {
    'draft': 'Draft',
    'pending_approval': 'Pending Approval',
    'assigned': 'Assigned',
    'in_progress': 'In Progress',
    # 'pending_review': 'Pending Review',
    'qa_review': 'QA Review',
    'pending_acceptance': 'Pending Acceptance',
    'done': 'Done',
}

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # -----------------------
    # Workflow State
    # -----------------------
    mono_state = fields.Selection([
        ('draft', 'Draft'),
        ('pending_approval', 'Pending Approval'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        # ('pending_review', 'Pending Review'),
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

    requester_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    approved_by = fields.Many2one('res.users')
    qa_by = fields.Many2one('res.users')

    # -----------------------
    # Compute Delay
    # -----------------------
    @api.depends('deadline', 'finished_date')
    def _compute_delay(self):
        for rec in self:
            if rec.deadline and rec.finished_date:
                rec.delay_days = int((rec.finished_date - rec.deadline).total_seconds() / 86400)
            else:
                rec.delay_days = 0

    # -----------------------
    # Track Deadline Change
    # -----------------------
    def write(self, vals):
        # track deadline extend
        if 'deadline' in vals:
            for rec in self:
                if rec.deadline:
                    rec.deadline_extend_count += 1

        res = super().write(vals)

        # sync state -> kanban
        if 'mono_state' in vals:
            for rec in self:
                rec._update_stage_from_state()

        # (optional) sync kanban -> state
        if 'stage_id' in vals and not self.env.context.get('from_mono'):
            for rec in self:
                rec._update_state_from_stage()

        return res

    # -----------------------
    # Create Sync
    # -----------------------
    @api.model
    def create(self, vals):
        task = super().create(vals)
        task._update_stage_from_state()
        return task

    # -----------------------
    # State → Stage
    # -----------------------
    def _update_stage_from_state(self):
        self.ensure_one()

        stage_name = MONO_STAGE_MAP.get(self.mono_state)
        if not stage_name:
            return

        stage = self.env['project.task.type'].search([
            ('name', '=', stage_name),
            '|',
            ('project_ids', '=', False),
            ('project_ids', 'in', self.project_id.id)
        ], limit=1)

        if stage:
            self.with_context(from_mono=True).stage_id = stage.id

    # -----------------------
    # Stage → State
    # -----------------------
    def _update_state_from_stage(self):
        self.ensure_one()

        for key, value in MONO_STAGE_MAP.items():
            if self.stage_id.name == value:
                self.mono_state = key
                break

    # -----------------------
    # Workflow Actions
    # -----------------------
    def action_submit(self):
        self.mono_state = 'pending_approval'

    def action_approve(self):
        self.mono_state = 'assigned'
        self.approved_by = self.env.user

    def action_reject(self):
        self.mono_state = 'draft'

    def action_start(self):
        self.mono_state = 'in_progress'

    def action_submit_review(self):
        self.mono_state = 'qa_review'

    def action_qa_pass(self):
        self.mono_state = 'pending_acceptance'
        self.qa_by = self.env.user

    def action_qa_fail(self):
        self.revision_count += 1
        self.mono_state = 'in_progress'

    def action_accept(self):
        self.mono_state = 'done'
        self.finished_date = fields.Datetime.now()