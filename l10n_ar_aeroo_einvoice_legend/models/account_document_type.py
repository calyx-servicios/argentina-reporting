from odoo import models, fields, api

class AcountDocumentType(models.Model):
    _inherit = 'account.document.type'

    default_legend = fields.Text(string = "Default legend")