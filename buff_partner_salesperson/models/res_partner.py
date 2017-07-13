# -*- coding: utf-8 -*-
# © <2017> <builtforfifty>

from openerp import models

class res_partner(models.Model):
	_inherit = 'res.partner'

	_defaults = {
		'user_id': lambda self, cr, uid, ctx=None: uid,
	}
