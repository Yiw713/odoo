{
    "name": "Mono Task Multi Project",
    "version": "2.0",
    "depends": ["project", "mail"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/project_data.xml",
        "data/task_stage_data.xml",
        "views/project_task_views.xml",
        "views/project_dashboard_views.xml",
        "views/project_views.xml",   
    ],
    "post_init_hook": "post_init_hook",
    "assets": {
        "web.assets_backend": [
            "mono_task_project/static/src/js/kanban_confirm.js",
        ],
    },
    "installable": True,
}