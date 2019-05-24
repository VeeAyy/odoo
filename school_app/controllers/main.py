from odoo import http

class Books(http.Controller):

    @http.route('/school/students', auth='public')

    def list(self, **kwargs):
        Student = http.request.env['school.student']
        students = Student.search([])
        return http.request.render('school_app.student_list_template', {'students': students})