# -*- coding: utf-8 -*-
# Copyright 2017 Giacomo Grasso, Gabriele Baldessari
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Validate Remaining Moves',
    'summary': """
        This module validates all picking's account moves even if the quantity or lots have been already specified in some moves""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Giacomo Grasso, Gabriele Baldessari, Odoo Community Association (OCA)',
    'depends': [
        'stock'
    ],
    'data': [
        'views/stock_backorder_confirmation.xml',
    ],
    'demo': [
    ],
}
