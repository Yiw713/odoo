{
    'name': "crm_custom",
    'version': '1.0',
    'author': "Yutthakarn",
    'license': 'LGPL-3',
    'depends': ['crm'],  
    'data': [
    'security/ir.model.access.csv',
    'data/crm_stage_data.xml',
    'data/currency_data.xml',
    'views/crm_lead_view.xml',  
],
'post_init_hook': 'update_crm_stages',

    'installable': True,
    'application': False,
}
