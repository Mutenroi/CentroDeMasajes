# -*- coding: utf-8 -*-
{
    'name': "Masajes",

    'summary': """Masajes""",
    
    'description': """
        Centro de masajes
    """,

    'icon': "/CentroDeMasaje/static/img/masaje.png",


    'author': "Grupo Prodev",
    'website': "https://www.bucmi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'RubricaFinal',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
