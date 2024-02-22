from odoo import models, api, fields

class Modulo(models.Model):
    _name = "modulo"

    modulo = fields.Char(string="Modulo", required=True)
    alumno_id = fields.Many2one('alumno', 'models_id', string="Alumno")
    ciclo_id = fields.Many2many('ciclo.formativo', 'models_id', string="Ciclo")
    profesor_id = fields.Many2one('profesor', 'models_id', string="Profesor")

    
