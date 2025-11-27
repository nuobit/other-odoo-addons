# Cybrosys Technologies - Anusha P P <odoo@cybrosys.com>
# Copyright 2025 NuoBiT Solutions - Deniz Gallo <dgallo@nuobit.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, fields, models
from odoo.exceptions import UserError


class VisitDetails(models.Model):
    _name = "fo.property.counter"
    _inherit = "mail.thread"
    _rec_name = "employee"
    _description = "Property Details"

    employee = fields.Many2one("hr.employee", required=True)
    date = fields.Date(required=True)
    visitor_belongings = fields.One2many(
        "fo.belongings",
        "belongings_id_fov_employee",
        string="Personal Belongings",
        copy=False,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("prop_in", "Taken In"),
            ("prop_out", "Taken out"),
            ("cancel", "Cancelled"),
        ],
        tracking=True,
        default="draft",
        help="If the employee taken the belongings to the company "
        'change state to ""Taken In""'
        'when he/she leave office change the state to ""Taken out""',
    )

    def action_cancel(self):
        self.state = "cancel"

    def action_prop_in(self):
        count = 0
        number = 0
        for data in self.visitor_belongings:
            if not data.property_count:
                raise UserError(_("Please Add the Count."))
            if data.permission == "1":
                count += 1
            number = data.number
        if number == count:
            raise UserError(_("No property can be taken in."))
        else:
            self.state = "prop_in"

    def action_prop_out(self):
        self.state = "prop_out"
