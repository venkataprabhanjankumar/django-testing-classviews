from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from users.models import User


class UserAuth(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            result = check_password(password, user.password)
            if result:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



# For token authentication
class TokenAuth(BaseBackend):
    def authenticate(self, request, **kwargs):
        pass
