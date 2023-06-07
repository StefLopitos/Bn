
from odoo import api,models
from odoo.addons.bn_sale.validators.sale_order_validator import SaleOrderValidator


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _order = 'id desc'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.ensure_one()
        SaleOrderValidator(self).validate_confirmation()
        return res

    def onclick_remove_qty_zero(self):
        for line in self.order_line:
            if line.product_uom_qty == 0:
                line.delete_line_product_qty_zero(line)
