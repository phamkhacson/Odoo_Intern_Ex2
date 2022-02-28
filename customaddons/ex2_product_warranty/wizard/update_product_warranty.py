from odoo import models, api, fields
from odoo.exceptions import ValidationError
import datetime


class UpdateWarranty(models.TransientModel):
    _name = "update.warranty"
    new_date_from = fields.Datetime(string="New Date From")
    new_date_to = fields.Datetime(string="New Date To")
    product_ids = fields.Many2many('product.template', string="Products")

    def save_update_warranty(self):
        for req in self.product_ids:
            req.date_from = self.new_date_from
            req.date_to = self.new_date_to
            if self.new_date_to < self.new_date_from:
                raise ValidationError("'Date to' must better than 'date from'")
            else:
                df = str(req.date_from.strftime('%d%m%y'))
                dt = str(req.date_to.strftime('%d%m%y'))
                req.product_warranty = 'PWR'+'/'+df+'/'+dt
                check = req.date_to.date() - datetime.datetime.now().date()
                if int(str(check).split(' ')[0]) < 0:
                    req.check_discount = True
                    req.discount = 'Discount 10%'
                    req.estimate_discount = req.list_price * 0.1
                    req.time_interval = '0'
                else:
                    req.check_discount = False
                    req.discount = 'Null'
                    req.estimate_discount = 0
                    req.time_interval = str(check).split(",")[0]
