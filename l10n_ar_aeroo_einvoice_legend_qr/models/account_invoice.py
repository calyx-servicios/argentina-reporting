from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    legend_in_document = fields.Text(string = "Legend in Document")

    @api.onchange('journal_document_type_id')
    def onchange_journal_document_type_id(self):
        
        legend_id = self.env['default.legend.document.company'].search([('company', '=', self.company_id.id),
                                                                        ('document_type', '=', self.document_type_id.id)])
        if legend_id:
            self.legend_in_document = legend_id.default_legend
