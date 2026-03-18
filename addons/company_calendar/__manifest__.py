{
    "name": "Company Calendar",
    "version": "1.0",
    "summary": "Company Events and Holidays Calendar",
    "description": "Manage company holidays and events in calendar view",
    "author": "Your Company",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        
        "views/event_views.xml",
        "views/event_type_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
}