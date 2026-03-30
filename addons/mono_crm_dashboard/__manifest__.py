{
    'name': 'Mono CRM Dashboard',
    'version': '1.0',
    'depends': ['crm', 'web'],
    'data': [
        'views/dashboard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'https://cdn.jsdelivr.net/npm/chart.js',
            'mono_crm_dashboard/static/src/js/dashboard.js',
            'mono_crm_dashboard/static/src/xml/dashboard_template.xml',
        ],
    },
    'installable': True,
}