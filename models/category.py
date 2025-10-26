from odoo import models, fields

class Category(models.Model):
    _name = "category"
    _description = "Device Category"

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text(string="Description")
    device_ids = fields.One2many('device', 'category_id', string='Devices')