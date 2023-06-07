# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError


class SaleOrderValidator:
    def __init__(self, sale_order):
        self._lines = sale_order.order_line
        self._message_validation = ''

    def validate_confirmation(self):
        self._validate_lines()
        if self._message_validation != '':
            raise ValidationError(self._message_validation)

    def _validate_lines(self):
        for line in self._lines:
            self.validate_product_qty_distinct_zero(line)

    def validate_product_qty_distinct_zero(self, line):
        if line.product_uom_qty < 1 and line.product_id.display_name not in self._message_validation:
            self._message_validation += '\n La cantidad a transferir debe ser mayor a 0 para el producto: {}.'.format(
                line.product_id.display_name)
