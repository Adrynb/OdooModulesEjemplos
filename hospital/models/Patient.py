# models/patient.py

from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'

    name = fields.Char(string='Nombre y apellidos')
    symptoms = fields.Text(string='Síntomas')
