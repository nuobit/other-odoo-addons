# Cybrosys Technologies - Anusha P P <odoo@cybrosys.com>
# Copyright 2025 NuoBiT Solutions - Deniz Gallo <dgallo@nuobit.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


{
    "name": "Front Office Management",
    "version": "18.0.1.0.0",
    "summary": """Manage Front Office Operations:
    Visitors, Devices Carrying Register, Actions""",
    "author": "Cybrosys Techno Solutions, NuoBiT Solutions SL",
    "maintainer": "Cybrosys Techno Solutions",
    "company": "Cybrosys Techno Solutions",
    "website": "https://github.com/nuobit/other-odoo-addons",
    "category": "Industries",
    "depends": ["base", "hr"],
    "data": [
        "views/fo_visit.xml",
        "views/fo_visitor.xml",
        "views/fo_property_counter.xml",
        "report/report.xml",
        "report/fo_property_label.xml",
        "report/fo_visitor_label.xml",
        "report/visitors_report.xml",
        "security/fo_security.xml",
        "security/ir.model.access.csv",
    ],
    "images": ["static/description/banner.png"],
    "license": "AGPL-3",
}
