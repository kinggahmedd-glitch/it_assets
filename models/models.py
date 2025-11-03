from odoo import models, fields, api



class Models(models.Model):
    _name = "models"
    _description = "device and assets Spec"

    name = fields.Char(string='Name',)
    category = fields.Many2one('category', string='Category', ondelete='set null')
