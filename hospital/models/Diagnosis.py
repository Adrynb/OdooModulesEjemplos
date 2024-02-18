# models/diagnosis.py

from odoo import models, fields

class Diagnosis(models.Model):
    _name = 'hospital.diagnosis'

    patient_id = fields.Many2one('hospital.patient', string='Paciente')
    doctor_id = fields.Many2one('hospital.doctor', string='Médico')
    diagnosis = fields.Text(string='Diagnóstico')
    symptoms = fields.Text(string='Síntomas', related='patient_id.symptoms', readonly=True)
    
