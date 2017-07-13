# -*- coding: utf-8 -*-
# © <2017> <builtforfifty>

from odoo import models, fields

class res_partner(models.Model):
	_inherit = 'res.partner'

	def _get_current_uid(self):
		return self.env.uid

	user_id = fields.Many2one(default=_get_current_uid)
