# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules, tools

class ResUsers(models.Model):
	_name = 'account.res_users'
	_inherit = "res.users"

	pasport = fields.Char(string='Паспортные данные', required=False)

