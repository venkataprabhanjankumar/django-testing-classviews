from django.urls import reverse

from tests.testcases import AuthenticateTestCases, TestCase


class TestLoginRequired(TestCase):
    def test_redirection(self):
        url_names = [
            'create_post',
            'create_book',
        ]
        for url_name in url_names:
            """
            Return a context manager that will return the enclosed block of code in a subtest
            identified by the optional message and keyword parameters. 
            A failure in the subtest marks the test case as failed but resumes
            execution at the end of the enclosed block, allowing further test code
            to be executed.
            """
            with self.subTest(url_name=url_name):
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertRedirectLoginRequired(response=response, url=url)
