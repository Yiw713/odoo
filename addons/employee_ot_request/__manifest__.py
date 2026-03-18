{
    'name': 'Employee OT Request',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'ระบบขออนุมัติทำงานล่วงเวลา (OT)',
    'depends': ['hr', 'mail','hr_work_entry'],
    'data': [
        'security/ir.model.access.csv',
        'views/ot_request_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}