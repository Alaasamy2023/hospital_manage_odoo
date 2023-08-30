# -*- coding: utf-8 -*-
{
    'name': 'hospital_manage_odoo',
    'version': '1.0.0',
    'summary': 'hospital_manage_odoo',
    'sequence': -100,
    'description': """Odoo 16 Development Tutorials""",
    'category': 'alaa samy',
    'author': 'Odoo alaa samy',
    'maintainer': 'odoo',
    'website': 'https://www.alaasamy.tech',
    'license': 'AGPL-3',
    'depends': ['mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/patient_gender_view.xml',

    ],
    'demo': [],
    'live_test_url': '',
    'installable': True,
    'application': True,
}
