
from odoo import  models, fields, api


class Device(models.Model):
    _name = "device"
    _description = "device and assets"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Code', required=True, copy=False, readonly=True, default='New')
    employee_id = fields.Many2one('hr.employee', string='Employee', tracking=True)
    department_id = fields.Many2one('hr.department',string='Department',related='employee_id.department_id',store=True,readonly=True)
    manufacturer_id = fields.Many2one('res.partner', string='Manufacturer')
    model = fields.Many2one('models', string='Model', domain="[('category', '=', category)]")
    mac_address = fields.Char(required=True, string='MAC Address')
    vendor_id = fields.Many2one('res.partner',string='Vendor',domain=[('supplier_rank', '>', 0)],tracking=True)
    notes = fields.Text()
    Purchase_Date = fields.Date()
    status = fields.Selection([
        ('active', 'Active'),
        ('in_maintenance', 'In Maintenance'),
        ('in_active', 'In active')
    ], string='Status', default='active', tracking=True)
    category = fields.Many2one('category', string='Category', ondelete='set null')
    specs_line_ids = fields.One2many('device.spec.line', 'device_id', string='Specifications')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('it.device') or 'New'
        return super(Device, self).create(vals)

    def action_set_active(self):
        for rec in self:
            rec.status = 'active'

    def action_set_in_maintenance(self):
        for rec in self:
            rec.status = 'in_maintenance'

    def action_set_in_active(self):
        for rec in self:
            rec.status = 'in_active'



class DeviceSpecLine(models.Model):
    _name = "device.spec.line"
    _description = "device and assets Spec"

    name = fields.Many2one('specs')
    value=fields.Char()
    device_id = fields.Many2one('device')


