from django.db import models
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=225, blank=False, null=False, unique=True,
                                error_messages="Username must me unique")
    email = models.EmailField(max_length=225, blank=False, null=False, unique=True,
                              error_messages="Email must be unique")
    password = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    last_login = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = "Users"

    def set_password(self, password):
        self.password = make_password(password)
        self.save()

    def __str__(self):
        return self.username


class Post(models.Model):
    created_by = models.CharField(max_length=225)
    post_name = models.CharField(max_length=225)
    post_description = models.CharField(max_length=225)

    class Meta:
        db_table = "Posts"

    def __str__(self):
        return self.post_name
