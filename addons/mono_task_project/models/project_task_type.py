from odoo import models, fields

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    stage_code = fields.Selection([
        ('draft', 'Draft'),
        ('pending_approval', 'Pending Approval'),
        ('reviewing', 'Reviewing'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('pending_review', 'Pending Review'),
        ('qa_review', 'QA Review'),
        ('pending_acceptance', 'Pending Acceptance'),
        ('done', 'Done'),
    ], string="Stage Code")

    mono_type = fields.Selection([
        ('internal', 'Internal'),
        ('outsource', 'Outsource'),
    ], string="Workflow Type")