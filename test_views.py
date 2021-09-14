from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class SiteConfigViewTestCase(TestCase):
    def setUp(self):
        self.siteConfigView = Client()
        self.siteConfigName = reverse_lazy("configs")

    def test_get(self):
        request = self.siteConfigView.get(self.siteConfigName)
        self.assertEquals(request.status_code, 302)

    def test_post(self):
        response = self.siteConfigView.post(self.siteConfigName)
        self.assertEquals(response.status_code, 302)


class SessionListViewTestCase(TestCase):
    def setUp(self):
        self.sessionList = Client()
        self.sessionName = reverse_lazy("sessions")

    def test_get_context_data(self):
        request = self.sessionList.get(self.sessionName)
        self.assertEquals(request.status_code, 302)


class SessionCreateViewTestCase(TestCase):
    def setUp(self):
        self.sessionCreate = Client()
        self.sessionName = reverse_lazy("session-create")

    def test_get_context_data(self):
        request = self.sessionCreate.get(self.sessionName)
        self.assertEqual(request.status_code, 302)


class SessionUpdateViewTestCase(TestCase):
    def setUp(self):
        self.sessionUpdate = Client()
        self.sessionName = reverse_lazy("sessions")

    def test_form_valid(self):
        request = self.sessionUpdate.get(self.sessionName)
        self.assertEqual(request.status_code, 302)


class SessionDeleteViewTesteCase(TestCase):
    def setUp(self):
        self.sessionDelete = Client()
        self.sessionName = reverse_lazy("sessions")

    def test_delete(self):
        request = self.sessionDelete.get(self.sessionName)
        self.assertEqual(request.status_code, 302)


class TermListViewTestCase(TestCase):
    def setUp(self):
        self.termList = Client()
        self.termName = reverse_lazy("terms")

    def test_get_context_data(self):
        request = self.termList.get(self.termName)
        self.assertEqual(request.status_code, 302)


class TermUpdateViewTestCase(TestCase):
    def setUp(self):
        self.termUpdate = Client()
        self.termName = reverse_lazy("terms")

    def test_form_valid(self):
        request = self.termUpdate.get(self.termName)
        self.assertEqual(request.status_code, 302)


class TermDeleteViewTestCase(TestCase):
    def setUp(self):
        self.termDelete = Client()
        self.termName = reverse_lazy("terms")

    def test_delete(self):
        request = self.termDelete.get(self.termName)
        self.assertEqual(request.status_code, 302)


class ClassListViewTestCase(TestCase):
    def setUp(self):
        self.classListView = Client()
        self.classListViewName = reverse_lazy("classes")

    def test_get_context_data(self):
        request = self.classListView.get(self.classListViewName)
        self.assertEqual(request.status_code, 302)


class ClassDeleteViewTestCase(TestCase):
    def setUp(self):
        self.classDeleteView = Client()
        self.classDeleteName = reverse_lazy("classes")

    def test_delete(self):
        request = self.classDeleteView.get(self.classDeleteName)
        self.assertEqual(request.status_code, 302)


class SubjectListViewTestCase(TestCase):
    def setUp(self):
        self.subjectListView = Client()
        self.subjectListName = reverse_lazy("subjects")

    def test_get_context_data(self):
        request = self.subjectListView.get(self.subjectListName)
        self.assertEqual(request.status_code, 302)


class SubjectDeleteViewTestCase(TestCase):
    def setUp(self):
        self.subjectDeleteView = Client()
        self.subjectDeleteName = reverse_lazy("subjects")

    def test_delete(self):
        request = self.subjectDeleteView.get(self.subjectDeleteName)
        self.assertEqual(request.status_code, 302)


class CurrentSessionAndTermViewTestCase(TestCase):
    def setUp(self):
        self.currentSession = Client()
        self.currentName1 = "current_session"
        self.currentName2 = "current_term"

    def test_get(self):
        request = self.currentSession.get(self.currentName1)
        request2 = self.currentSession.get(self.currentName2)
        self.assertEquals(request.status_code, 404)
        self.assertEquals(request2.status_code, 404)

    def test_post(self):
        response = self.currentSession.post(self.currentName1)
        response2 = self.currentSession.post(self.currentName2)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response2.status_code, 404)
