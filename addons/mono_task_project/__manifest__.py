{
    "name": "Mono Task (Project Extension)",
    "version": "1.0",
    "depends": ["project", "mail"],
    "author": "Mono",
    "category": "Project",
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/project_task_views.xml",
        "views/project_dashboard_views.xml",
    ],
    "installable": True,
    "application": False,
    'assets': {
    'web.assets_backend': [
        'mono_task_project/static/src/js/kanban_confirm.js',
    ],
},
}