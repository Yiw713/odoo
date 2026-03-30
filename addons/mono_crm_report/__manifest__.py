{
    'name': 'Mono CRM Report',
    'version': '1.0',
    'depends': ['crm', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_report_views.xml',
    ],
    'installable': True,
}