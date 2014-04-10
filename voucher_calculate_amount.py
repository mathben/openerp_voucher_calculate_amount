# -*- encoding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openerp.osv import orm


class voucher_calculate_amount(orm.Model):
    _inherit = "account.voucher"

    def sum_amount(self, cr, uid, ids, context=None):
        self.browse(cr, uid, ids, context=context)
        pool_account_amount = self.browse(cr, uid, ids, context=context)
        for account in pool_account_amount:
            credit = [line.amount for line in account.line_cr_ids]
            debit = [line.amount for line in account.line_dr_ids]
            if account.type == "payment":
                amount = sum(debit) - sum(credit)
            else:
                amount = -sum(debit) + sum(credit)
            data = {"amount": amount}
            account.write(data, context=context)
