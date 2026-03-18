{
    'name': 'Mono Company Calendar',
    'version': '1.0',
    'summary': 'Company Event and Holiday Calendar',
    'description': """
        Company Calendar for Mono Organization
        - Company Holidays
        - Company Events
        - Company Activities
    """,
    'author': 'Mono',
    'category': 'Productivity',
    'depends': ['calendar'],
    'data': [
        'security/ir.model.access.csv',

        'data/mono_calendar_data.xml',

        'views/mono_calendar_views.xml',
        'views/mono_calendar_search.xml',
        'views/mono_calendar_menu.xml',
    ],
    'installable': True,
    'application': False,
}