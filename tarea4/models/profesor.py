from odoo import models, fields

class Profesor(models.Model):
    _name = "tarea4.profesor"

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Integer(string="DNI", required=True)
    models_id = fields.One2many("tarea4.modulo", "profesor_id", string="Módulos", readonly=True)
