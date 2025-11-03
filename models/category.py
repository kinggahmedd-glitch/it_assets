from odoo import models, fields

class Category(models.Model):
    _name = "category"
    _description = "Device Category"

    name = fields.Char(string="Name", required=True)