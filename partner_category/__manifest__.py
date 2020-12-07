# -*- coding: utf-8 -*-
{
    "name": "Partner Category",
    "version": "13.1.1",
    'license': 'LGPL-3',
    'author': '',
    'company': '',
    'website': '',
    "summary": """
    Add partner category multi-company
    """,
    "description": """
Add partner category multi-company
=========================
Automatically create the customer number from a sequence when a customer is being created.

The customer number can be configured in the sequence "Customer Number".
    """,
    "category": "Sales",
    "depends": [
        "base",
        "sale","contacts","product","account",
    ],
    "data": [
        "data/sequencer.xml",
        "views/partner.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "auto_install": False,
}
