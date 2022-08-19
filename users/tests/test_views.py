from django.urls import reverse, resolve

from tests.testcases import AuthenticateTestCases, TestCase
from users import views
from users.models import Post


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


class TestPostCreation(AuthenticateTestCases):
    def setUp(self):
        super().setUp()
        url = reverse('create_book')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_url_resolves_correct_view(self):
        view = resolve(reverse('create_post'))
        self.assertEqual(view.func.view_class, views.CreatePost)

    def test_html_content(self):
        contents = (
            ('<input type="hidden"', 1),  # for csrf
            ('<input type="text"', 2),  # for name,description
            ('<input type="number"', 1),  # for price
        )
        for content in contents:
            with self.subTest(content=content[0]):
                self.assertContains(self.response, content[0], content[1])


class TestPostCreationSuccess(AuthenticateTestCases):
    def setUp(self):
        super().setUp()
        self.url = reverse('create_post')
        self.data = {
            'post_name': 'post1',
            'post_description': 'Post Description 1',
            'created_by': self.user.username
        }
        self.response = self.client.post(self.url, self.data)

    def test_redirection(self):
        self.assertEqual(self.response.url, reverse('list_posts'))
        self.assertRedirects(self.response, reverse('list_posts'))

    def test_post(self):
        self.assertEqual(Post.objects.get(post_name='post1').post_name, 'post1')
