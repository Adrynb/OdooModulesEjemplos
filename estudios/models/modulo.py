from odoo import models, api, fields
class Modulo(models.Model):
    _name = "estudios.modulo"

    modulo = fields.Char(string="Modulo", required=True)
    alumno_id = fields.Many2many('estudios.alumno', string="Alumno", readonly=True)
    ciclo_id = fields.Many2one('estudios.ciclo', string="Ciclo", readonly=True)
    profesor_id = fields.Many2one('estudios.profesor', string="Profesor", readonly=True)
