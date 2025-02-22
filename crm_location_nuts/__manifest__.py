# Copyright 2015 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# Copyright 2017 David Vidal <david.vidal@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NUTS Regions in CRM",
    "category": "Customer Relationship Management",
    "version": "16.0.1.0.0",
    "depends": [
        "crm",
        "sales_team",
        "base_location_nuts",
    ],
    "data": [
        "views/crm_lead_view.xml",
    ],
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/crm",
    "license": "AGPL-3",
    "installable": True,
    "maintainers": ["rafaelbn", "edlopen"],
}
