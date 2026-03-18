{
    'name': 'Mono Request System',
    'version': '1.0',
    'summary': 'Request & Approval System',
    'category': 'Tools',
    'author': 'Mono',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/request_views.xml',
    ],
    'installable': True,
    'application': True,
}