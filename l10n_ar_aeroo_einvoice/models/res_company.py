##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'
    _name = 'res.company'

    logo_invoice = fields.Binary(string="Company Invoice Logo")