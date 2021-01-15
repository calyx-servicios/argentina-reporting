# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Argentinian Payment Aeroo Report Extend",
    "summary": """
        """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["Lolstalgia"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # for the full list
    "category": "Report",
    "version": "11.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    # any module necessary for this one to work correctly
    "depends": ["base", "l10n_ar_aeroo_payment_group"],
    # always loaded
    "data": ["report/payment_report.xml"],
}
