# -*- coding: utf-8 -*-
# © <2017> <builtforfifty>

from openerp import fields, models

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    branch = fields.Char(string="Branch Code")
