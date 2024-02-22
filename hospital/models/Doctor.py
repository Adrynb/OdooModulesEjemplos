# models/doctor.py

from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char(string='Nombre y apellidos')
    registration_number = fields.Char(string='Número de colegiado')
    _diagnosis_id = fields.One2many('hospital.diagnosis', 'doctor_id', string="Diagnositco",
    readonly=True )
