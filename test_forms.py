from django.test import TestCase
from ..forms import AcademicSessionForm, AcademicTermForm, SubjectForm, StudentClassForm


class AcademicSessionFormTestCase(TestCase):
    def setUp(self):
        self.name = "test session"
        self.current = True

        self.dados = {
            'name': self.name,
            'current': self.current
        }

        self.form = AcademicSessionForm(data=self.dados)

    def test_academicSessionForm(self):
        session = StudentClassForm.is_valid(self.form)
        self.assertEqual(session, True)


class AcademicTermFormTestCase(TestCase):
    def setUp(self):
        self.name = "Academic Term"
        self.current = False

        self.dados = {
            "name": self.name,
            "current": self.current
        }

        self.form = AcademicTermForm(data=self.dados)

    def test_academicTermSession(self):
        session = StudentClassForm.is_valid(self.form)
        self.assertEqual(session, True)


class SubjectFormTestCase(TestCase):
    def setUp(self):
        self.name = "Subject Form"

        self.dados = {
            "name": self.name,
        }

        self.form = SubjectForm(data=self.dados)

    def test_subjectForm(self):
        session = StudentClassForm.is_valid(self.form)
        self.assertEqual(session, True)


class StudentClassFormTestCase(TestCase):
    def setUp(self):
        self.name = "Student Session"

        self.dados = {
            "name": self.name,
        }

        self.form = StudentClassForm(data=self.dados)

    def test_studentClassForm(self):
        session = StudentClassForm.is_valid(self.form)
        self.assertEqual(session, True)
