{
    'name': 'Mono CRM Analytics',
    'version': '1.0',
    'summary': 'CRM Analytics Dashboard',
    'depends': ['crm', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_dashboard.xml',
        'views/crm_unfollowed_views.xml',
    ],
    'installable': True,
}