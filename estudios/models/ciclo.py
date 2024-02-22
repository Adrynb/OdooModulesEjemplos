from odoo import models, api, fields 

class Ciclo(models.Model):
    _name = 'ciclo.formativo'
    
    name = fields.Char(string="Nombre", required = True)
    models_id = fields.One2many("modulo", "ciclo_id", string="Modulos")
    
