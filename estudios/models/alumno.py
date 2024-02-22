from odoo import models, api, fields 


class Alumno(models.Model):
    _name = "alumno"

    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string = "Apellidos", required = True)
    dni = fields.Integer(string = "DNI", required = True)
    models_id = fields.One2many('modulo', 'profesor_id', string = "Modulos")

