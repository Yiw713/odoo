from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    mono_type = fields.Selection([
        ('internal', 'Internal'),
        ('outsource', 'Outsource'),
    ], default='internal')

    @api.model
    def create(self, vals):
        project = super().create(vals)

        # 👇 assign stage ทันที
        stages = self.env['project.task.type'].search([
            ('mono_type', '=', project.mono_type)
        ])

        for stage in stages:
            stage.write({
                'project_ids': [(4, project.id)]
            })

        return project