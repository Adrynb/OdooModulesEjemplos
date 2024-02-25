from odoo import models, api, fields 

class Modulo(models.Model):
    _name = "tarea4.modulo"
    _rec_name ="ciclo_id"
    _rec_name ="profesor_id"

    modulo = fields.Char(string="Modulo", required = True)
    ciclo_id = fields.Many2one("tarea4.ciclo", string="Ciclo")
    alumno_id = fields.Many2many("tarea4.alumno", string="Alumno")
    profesor_id = fields.Many2one("tarea4.profesor", string="Profesor")
