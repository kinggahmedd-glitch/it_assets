from odoo import models, fields

class Specs(models.Model):
    _name = "specs"


    name = fields.Char(string="Specification Name", required=True)
    value = fields.Char(string='Value')
    description = fields.Text(string="Description")
    device_id = fields.Many2one('device', string='Device', ondelete='cascade')