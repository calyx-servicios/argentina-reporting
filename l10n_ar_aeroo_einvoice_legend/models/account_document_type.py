from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError

class DefaultLegendDocumentCompany(models.Model):
    _name = 'default.legend.document.company'

    default_legend = fields.Text(string = "Default legend")
    company = fields.Many2one('res.company')
    document_type = fields.Many2one('account.document.type')

    @api.constrains('company','document_type')
    @api.multi
    def _check_unique_record(self):

        records = self.env['default.legend.document.company'].search([('company', '=', self.company.id),
                                                                      ('document_type', '=', self.document_type.id)])
        if len(records) > 1 :
            raise ValidationError(_('La configuracion por tipo de documento y compañia debe ser unica'))
