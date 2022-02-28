import datetime
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductWarranty(models.Model):
    _inherit = 'product.template'
    product_warranty = fields.Text(string="Warranty", readonly="1")
    date_from = fields.Datetime(string="Date From")
    date_to = fields.Datetime(string="Date To")
    check_discount = fields.Boolean(string="check_discount", readonly="1")
    discount = fields.Char(string='Discount', readonly="1")
    estimate_discount = fields.Float(string="Total Discount", readonly="1")
    time_interval = fields.Char(string="Time Interval", readonly="1")

    @api.onchange('date_from', 'date_to')
    def onchange_date(self):
        if not self.date_to or not self.date_from:
            self.check_discount = True
            self.discount = 'Discount 10%'
            self.estimate_discount = self.list_price * 0.1
            self.time_interval = '0'
        else:
            if self.date_to < self.date_from:
                raise ValidationError("'Date to' must better than 'date from'")
            else:
                df = str(self.date_from.strftime('%d%m%y'))
                dt = str(self.date_to.strftime('%d%m%y'))
                self.product_warranty = 'PWR'+'/'+df+'/'+dt
                check = self.date_to.date() - datetime.datetime.now().date()
                if int(str(check).split(' ')[0]) < 0:
                    self.check_discount = True
                    self.discount = 'Discount 10%'
                    self.estimate_discount = self.list_price * 0.1
                    self.time_interval = '0'
                else:
                    self.check_discount = False
                    self.discount = 'Null'
                    self.estimate_discount = 0
                    self.time_interval = str(check).split(",")[0]

    def update_warranty_action(self):
        products = self.env['product.template'].browse(self.env.context.get('active_ids', []))
        view_form = self.env.ref('ex2_product_warranty.update_warranty_form').id
        return {
            'name': 'Update Warranty',
            'view_mode': 'form',
            'res_model': 'update.warranty',
            'views': [(view_form, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {
                'default_product_ids': products.ids
            }
        }

