# -*- coding: utf-8 -*-
{
    'name': "estudios",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
     'sequence': 1,

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
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
        'security/ir.model.access.csv',
        'views/modulo_views.xml',
        'views/alumno_views.xml',
        'views/ciclo_views.xml',
        'views/profesor_views.xml',
        'views/menu_personas.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

