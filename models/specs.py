from odoo import models, fields

class Specs(models.Model):
    _name = "specs"


    name = fields.Char(string='Name', ondelete='cascade')

    _sql_constraints = [
        ('unique_specs_name', 'unique(name)', 'Name must be unique!')
    ]