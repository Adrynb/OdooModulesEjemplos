from odoo import models, api, fields 

class Ciclo(models.Model):
    _name = 'estudios.ciclo'
    
    ciclo = fields.Char(string="Ciclo", required = True)
    modulos_id = fields.One2many("estudios.modulo", "ciclo_id", string="Modulos")
    
