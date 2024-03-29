from odoo import models, api, fields

class Profesor(models.Model):
    _name = "estudios.profesor"

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Integer(string="DNI", required=True)
    modulos_ids = fields.One2many('estudios.modulo', 'profesor_id', string="Modulos")