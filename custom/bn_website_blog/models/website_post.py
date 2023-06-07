from odoo import api, models, fields


class BlogPost(models.Model):
    _inherit = 'blog.post'

    company_id = fields.Many2one(comodel_name='res.company', string='Compañía', related="blog_id.company_id")
