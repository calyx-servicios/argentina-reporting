from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    legend_in_document = fields.Text(string = "Legend in Document", compute="compute_journal_document_type_id")
    
    @api.multi
    @api.depends('journal_document_type_id','company_id')
    def compute_journal_document_type_id(self):
        if self.company_id and self.journal_document_type_id:

            legend_id = self.env['default.legend.document.company'].search([('company', '=', self.company_id.id),
                                                                            ('document_type', '=', self.document_type_id.id)])
            if legend_id:
                if self.legend_in_document == "Add a comment to your report..." or not self.legend_in_document:
                    self.legend_in_document = legend_id.default_legend