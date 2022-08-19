from factory.django import DjangoModelFactory
import factory
from users.models import User


class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: f'user_{n}')
    password = factory.PostGenerationMethodCall('set_password', '123')
    email = factory.Sequence(lambda n: f'user_{n}@gmail.com')

    class Meta:
        model = User
        django_get_or_create = ('username',)
