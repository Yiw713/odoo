{
    'name': 'Mono CRM Note Template',
    'version': '1.0',
    'summary': 'CRM Note Template / Source / Product Helper',
    'category': 'CRM',
    'depends': ['crm', 'mail'],
    'data': [
        
    ],
    'assets': {
        'web.assets_backend': [
            'crm_note_template/static/src/js/note_template.js',
            'crm_note_template/static/src/xml/note_template.xml', 
        ],
    },
    'installable': True,
    'application': False,
}