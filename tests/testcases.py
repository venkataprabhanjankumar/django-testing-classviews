from django.test import TestCase as DjangoTestCase
from django.urls import reverse

from users.tests.factories import UserFactory


class TestCase(DjangoTestCase):
    """
    The HyperText Transfer Protocol (HTTP) 302 Found redirect status response code
     indicates that the resource requested has been temporarily moved to the URL given by the Location header
    """
    """Reverse_lazy is, as the name implies, a lazy implementation of the reverse URL resolver. Unlike the 
    traditional reverse function, reverse_lazy won't execute until the value is needed. It is useful because it 
    prevent Reverse Not Found exceptions when working with URLs that may not be immediately known. """

    def assertRedirectLoginRequired(self, response, url, status_code=302, target_status_code=200,
                                    msg_prefix='', fetch_redirect_response=True):
        login_url = reverse('signin')
        next_url = f'{login_url}?next={url}'
        return self.assertRedirects(response, next_url, status_code, target_status_code, msg_prefix,
                                    fetch_redirect_response)


class AuthenticateTestCases(TestCase):
    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.client.login(username=self.user.username, password='123')
