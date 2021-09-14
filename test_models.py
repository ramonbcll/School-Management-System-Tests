from django.test import TestCase
# from model_mommy import mommy
# from model_bakery import baker

from apps.corecode.models import (
    AcademicSession,
    AcademicTerm,
    SiteConfig,
    Subject,
    StudentClass,
)

"""
class InvoiceTestCase(TestCase):

    def setUp(self):
        self.estudante = baker.make('Student')

    def test_student(self):
        self.assertEqual(str(self.estudante), self.estudante.firstname)
"""


class SiteConfigTestCase(TestCase):
    def test_siteconfig(self):
        site_config = SiteConfig.objects.create(key="akey", value="aname")
        self.assertEqual(str(site_config), "akey")


class AcademicSessionTestCase(TestCase):
    def test_academicsession(self):
        session = AcademicSession.objects.create(name="test session", current=True)
        self.assertEqual(str(session), "test session")


class AcademicTermTestCase(TestCase):
    def test_academicterm(self):
        term = AcademicTerm.objects.create(name="test Term", current=True)
        self.assertEqual(str(term), "test Term")


class SubjectTestCase(TestCase):
    def test_subject(self):
        subject = Subject.objects.create(name="a_subject")
        self.assertEqual(str(subject), "a_subject")


class StudentClassTestCase(TestCase):
    def test_student(self):
        student = StudentClass.objects.create(name="test std")
        self.assertEqual(str(student), "test std")
