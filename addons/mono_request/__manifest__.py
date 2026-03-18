{
    'name': 'Mono Request',
    'version': '1.0',
    'summary': 'Internal Request Management',
    'author': 'Mono',
    'depends': ['project', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/mono_request_tree.xml',
    'views/mono_request_views.xml',
    'views/mono_request_kanban.xml',
    ],
    'installable': True,
}