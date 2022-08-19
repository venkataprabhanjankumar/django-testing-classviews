from django import forms
from django.contrib.auth.hashers import make_password

from .models import User, Post
from demo.models import Book


class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super(SignUp, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class SignIn(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class Demo(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print("Emails Sent")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_by',)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if commit:
            post.save()
        return post


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('created_by',)
