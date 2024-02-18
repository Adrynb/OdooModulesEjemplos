# -*- coding: utf-8 -*-
{
    'name': "Centro de Salud",

    'summary': "Modulo destinado a gestionar el centro de salud, donde se gestiona los medicos y pacientes que hay",

    'description': """
Modulo destinado a gestionar el centro de salud, donde se gestiona los medicos y pacientes que hay
    """,

    'author': "Adrian Navarro Buceta",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/diagnosis_views.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/menu_items.xml',
        'security/ir.model.access.csv',
    ]
    # only loaded in demonstration mode
    
}

