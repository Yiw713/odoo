{
    'name': 'Odoo Mono Custom',
    'version': '1.0',
    'summary': 'API + Dashboard + Cron Template',
    'author': 'Mono',
    'depends': ['base', 'web'],
    'data': [
    'security/ir.model.access.csv',
    'views/api_data_views.xml',
    'views/dashboard_views.xml',
    'views/menu.xml',
    'data/cron.xml',
],
    'installable': True,
    'application': True,
}