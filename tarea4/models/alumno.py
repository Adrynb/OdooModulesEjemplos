from odoo import models, api, fields 

class Alumno(models.Model):
    _name = "tarea4.alumno"

    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string = "Apellidos", required = True)
    dni = fields.Integer(string = "DNI", required = True)
    models_id = fields.Many2many('tarea4.modulo', string = "Modulos",
    readonly=True 
    )

