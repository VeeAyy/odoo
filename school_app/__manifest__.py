{
    'name': 'School Management',
    'description': 'Manage name and age of students.',
    'author': 'Vinh Huynh',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/school_menu.xml',
        'views/student_view.xml',
        'views/student_list_template.xml',
    ]
}