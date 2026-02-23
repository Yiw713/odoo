def update_crm_stages(cr, registry):
    from odoo.api import Environment
    env = Environment(cr, 1, {})

    stage_map = {
        'New': 'Mono_New',
        'Qualified': 'Mono_Qualified',
        'Proposition': 'Mono_Qualified',
        'Won': 'Mono_Qualified',
    }

    stages = env['crm.stage'].search([])
    for stage in stages:
        if stage.name in stage_map:
            stage.name = stage_map[stage.name]
