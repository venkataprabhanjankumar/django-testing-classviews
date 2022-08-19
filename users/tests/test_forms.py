from tests.testcases import TestCase
from django.utils import timezone
from users.forms import SignUp


class TestLoginForm(TestCase):
    def setUp(self):
        self.data = {
            'last_login': timezone.now(),
            'email': 'prabhanjan@gmail.com',
            'name': 'Prabhanjan',
            'username': 'prabhanjan',
            'password': '****@123'
        }

    def test_form_valid(self):
        form = SignUp(data=self.data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.data['email'] = 'hello'
        form = SignUp(data=self.data)
        self.assertFalse(form.is_valid())

