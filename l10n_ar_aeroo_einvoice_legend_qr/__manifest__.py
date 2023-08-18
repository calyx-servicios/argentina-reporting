# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Aeroo Invoice default legend on document type',
    'summary': """
        You can extend the legend in the document settings, 
        it can be reflected in the printing of the invoice. 
        You can also edit the default legend from the invoice form.
        The module is adapted to the new AFIP regulations that 
        includes a QR code in Argentine electronic invoices..""",

    'author': 'Calyx Servicios S.A., Odoo Community Association (OCA)',
    'maintainers': ['Milton Guzman'],

    'website': 'http://odoo.calyx-cloud.com.ar/',
    'license': 'AGPL-3',

    'category': 'Technical Settings',
    'version': '11.0.1.0.1',
    # see https://odoo-community.org/page/development-status
    'development_status': 'Production/Stable',

    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['l10n_ar_aeroo_einvoice'],

    'data': [
        'security/ir.model.access.csv',
        'views/account_document_type.xml',
        'views/account_invoice_form.xml',
        'views/invoice_report.xml',
        'views/report_configuration_defaults_data.xml',
        'views/invoice_report.xml',
    ],
}
