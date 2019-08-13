# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError


class AccountInvoiceRefund(models.TransientModel):
    """Credit Notes"""

    _inherit = "account.invoice.refund"


    @api.multi
    def compute_refund(self, mode='refund'):
        result = super(AccountInvoiceRefund, self).compute_refund(mode='refund')
        context = dict(self._context or {})
        inv_obj = self.env['account.invoice']
        for inv in inv_obj.browse(context.get('active_ids')):
            if result['domain'] and result['domain'][1][2]: # Factura proveedor  
                for refund_inv in inv_obj.browse(result['domain'][1][2]):
                    if inv.type in ('in_invoice','out_invoice'):
                        refund_inv.origin = _(inv.journal_document_type_id.document_type_id.name) +_(' N° ')+ _(refund_inv.origin)
        return result