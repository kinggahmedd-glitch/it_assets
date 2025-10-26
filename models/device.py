from email.policy import default

from odoo import  models, fields


class Device(models.Model):
    _name = "device"
    _description = "device and assets"

    name = fields.Char(required=1)
    category = fields.Char(required=1)
    employee = fields.Char(required=1)
    department = fields.Char(required=1)
    manufacturer = fields.Char(required=1)
    model = fields.Char(required=1)
    vendor = fields.Char(required=1)
    notes = fields.Text(required=1)
    Purchase_Date = fields.Date(required=1)
    status = fields.Selection([
        ('active','Active'),
        ('in_maintenance','In Maintenance'),
        ('in_active','In Active')
    ],default='active')
    category_id = fields.Many2one('category', string='Category', ondelete='set null')
    specs_line_ids = fields.One2many('specs', 'device_id', string='Specifications')





