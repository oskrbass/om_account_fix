# -*- coding: utf-8 -*-
{
	'name': "Ajuste de contabilidad",
	'category': 'Extra Tools',
	'version': '17.1',
	'author': 'Autores de Odoo',
	'depends': ['base', 'sale', 'product', 'account', 'stock','stock_account'],

	'summary': """
		Modifications related to sales for Faicery
	""",
	'description': """
		Modifications related to sales for Faicery
	""",
	'data': [
		"views/account_move.xml"
	],
	'images': [],
	'license': 'LGPL-3',
	'installable': True,
	'auto_install': False,
	'application': False,
}