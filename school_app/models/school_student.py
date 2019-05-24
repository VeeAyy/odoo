from odoo import  fields,  models

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'
    name = fields.Char('Name',size = 30 ,required = True)
    age = fields.Integer('Age')
