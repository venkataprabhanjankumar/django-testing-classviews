from django.test import TestCase
from users.models import User
from users.tests.factories import UserFactory
from django.contrib.auth.hashers import check_password


class TestUser(TestCase):
    def setUp(self):
        user = User.objects.create(username='prabhanjan', password='prabha')
        self.userid = user.pk

    def test_user(self):
        self.assertEqual(User.objects.get(pk=self.userid).pk, self.userid)

    def test_user_username(self):
        self.assertEqual(User.objects.get(pk=self.userid).username, 'prabhanjan')

    def test_user_login(self):
        user = UserFactory()
        print(user.password)
        self.assertTrue(check_password('123', user.password))
