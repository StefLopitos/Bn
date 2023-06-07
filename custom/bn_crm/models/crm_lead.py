import re

from odoo import api, models, fields

from odoo.addons.bn_crm.validators.crm_lead_validator import LeadValidator

SOURCE_TYPE = [('third_party', 'Terceros'), ('socail_network', 'Redes Sociales'),('internet_search','Busqueda en Internet')]


class Lead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self,vals):
        res = super(Lead, self).create(vals)
        LeadValidator(res).validate_create()
        return res

    source_type = fields.Selection(string='Fuente', selection=SOURCE_TYPE)
