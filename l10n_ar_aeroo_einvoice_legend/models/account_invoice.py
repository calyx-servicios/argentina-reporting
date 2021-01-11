from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    legend_in_document = fields.Text(string = "Legend in Document")

    @api.onchange('journal_document_type_id')
    def onchange_journal_document_type_id(self):
        self.legend_in_document = self.document_type_id.default_legend
