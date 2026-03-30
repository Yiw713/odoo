from odoo import api, SUPERUSER_ID

def post_init_hook(env):   # 👈 เปลี่ยนตรงนี้

    projects = env['project.project'].search([
        ('mono_type', '!=', False)
    ])

    for project in projects:
        stages = env['project.task.type'].search([
            ('mono_type', '=', project.mono_type)
        ])

        for stage in stages:
            if project.id not in stage.project_ids.ids:
                stage.write({
                    'project_ids': [(4, project.id)]
                })