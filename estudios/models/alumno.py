from odoo import models, api, fields 


class Alumno(models.Model):
    _name = "estudios.alumno"

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Integer(string="DNI", required=True)
    modulos_ids = fields.Many2many('estudios.modulo', string="Modulos")

