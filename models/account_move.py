# -*- coding: utf-8 -*-
from odoo import fields, models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_to_draft_single(self):
        for record in self:
            if record.state == 'posted':
                record.button_draft()


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    def action_update_value_with_standard_price(self):
        for layer in self:
            if layer.product_id and layer.product_id.standard_price:
                layer.value = layer.product_id.standard_price * abs(layer.quantity)