from odoo.tests import common


class TestSaleOrder(common.TransactionCase):

    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.SaleOrder = self.env['sale.order']
        self.Product = self.env['product.product']

    def test_check_product_quantities(self):
        # Create test products
        product1 = self.Product.create({'name': 'Producto 1', 'quantity': 10})
        product2 = self.Product.create({'name': 'Producto 2', 'quantity': 0})

        # Create a sales order with valid products (quantities other than zero)
        order1 = self.SaleOrder.create({'name': 'Orden de Venta 1'})
        order1.order_line.create({
            'order_id': order1.id,
            'product_id': product1.id,
            'product_uom_qty': 5,
        })
        self.assertEqual(order1.state, 'draft')  # The sell order should be in draft status.

        # Create a sales order with an invalid product (zero quantity)
        with self.assertRaises(Exception):
            order2 = self.SaleOrder.create({'name': 'Orden de Venta 2'})
            order2.order_line.create({
                'order_id': order2.id,
                'product_id': product2.id,
                'product_uom_qty': 3,
            })

        # Verify that the sales orders were created correctly
        self.assertTrue(order1)
        self.assertFalse('order2' in locals())  # Invalid sell order should not exist

        # Updating a sales order line to an invalid quantity (zero)
        order1.order_line[0].product_uom_qty = 0
        with self.assertRaises(Exception):
            order1.action_confirm()  # Should throw a validation exception

        # Verify that the sales order was not confirmed due to invalid quantity
        self.assertEqual(order1.state, 'draft')

        # Update the sales order line to a valid quantity and confirm the order.
        order1.order_line[0].product_uom_qty = 2
        order1.action_confirm()  # Should not throw exceptions
        self.assertEqual(order1.state, 'sale')  # The sell order should be in the sell status.
