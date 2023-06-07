from odoo import api, models, fields


class Blog(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one(comodel_name='res.company', string='Compañía')
