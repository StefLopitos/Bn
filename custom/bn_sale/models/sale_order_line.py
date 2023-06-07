# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def delete_line_product_qty_zero(self, line):
        query = """  DELETE FROM sale_order_line WHERE id =(%(line_id)s) """
        self.env.cr.execute(query, {
            "line_id": line.id
        })
