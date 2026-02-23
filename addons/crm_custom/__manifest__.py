{
    'name': "crm_custom",
    'version': '1.0',
    'author': "Yutthakarn",
    'license': 'LGPL-3',
    'depends': ['crm'],  
    'data': [
    'security/ir.model.access.csv',
    'data/crm_stage_data.xml',
    'views/crm_lead_view.xml',
    'views/crm_followup_views.xml',
    'views/crm_followup_dashboard_views.xml',
    # 'views/crm_custom_menu.xml',
    # 'views/crm_custom_action.xml',
    # 'views/crm_custom_kanban.xml',
    # 'views/crm_custom_form.xml',
    
],
'post_init_hook': 'update_crm_stages',

    'installable': True,
    'application': False,
}
