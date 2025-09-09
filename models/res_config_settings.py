from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    whatsapp_number = fields.Char(
        string="WhatsApp Number",
        config_parameter='whatsapp_float_button.number',
        help="Ingrese el Número en formato internacional, e.g. 56912345678"
    )
