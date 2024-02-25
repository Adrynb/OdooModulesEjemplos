from odoo import models, api, fields 

class Ciclo(models.Model):
    _name = "tarea4.ciclo"

    ciclo = fields.Char(string="Ciclo", required = True)
    models_id = fields.One2many( 'tarea4.modulo', 'ciclo_id', string="Modulos", 
    readonly=True)