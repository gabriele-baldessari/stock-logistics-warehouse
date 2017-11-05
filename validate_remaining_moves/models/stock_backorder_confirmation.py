# -*- coding: utf-8 -*-
# Copyright 2017 Giacomo Grasso, Gabriele Baldessari
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, _


class StockBackorderConfirmation(models.TransientModel):

    _inherit = 'stock.backorder.confirmation'

    @api.one
    def _process_remaining(self, cancel_backorder=False):
        for pack in self.pick_id.pack_operation_ids:
            if pack.qty_done > 0:
                pack.product_qty = pack.qty_done
            if pack.qty_done == 0:
                pack.qty_done = pack.product_qty
        self.pick_id.do_transfer()
        if cancel_backorder:
            backorder_pick = self.env['stock.picking'].search([
                ('backorder_id', '=', self.pick_id.id)])
            backorder_pick.action_cancel()
            body = _("Back order <em>%s</em> <b>cancelled</b>.")
            self.pick_id.message_post(body % (backorder_pick.name))

    @api.multi
    def validate_remaining_and_backorder(self):
        self._process_remaining()

    @api.multi
    def validate_remaning_no_backorder(self):
        self._process_remaining(cancel_backorder=True)
