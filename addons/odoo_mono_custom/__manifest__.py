{
    'name': 'Odoo Mono Custom',
    'version': '1.0',
    'summary': 'API + Dashboard + Cron Template',
    'author': 'Mono',
    'depends': ['base', 'web'],
    'data': [
    'security/ir.model.access.csv',
    'views/mono_login_views.xml',
    'views/api_data_views.xml',
    'views/dashboard_views.xml',
    'views/menu.xml',
    'views/seat_bus_views.xml',
    'data/cron.xml',
],
    'installable': True,
    'application': True,
}