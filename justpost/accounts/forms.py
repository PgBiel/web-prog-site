from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from posts.models import Post


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    # class Meta:
    #     model = User
    #     fields = ["username", "password"]
    #     widgets = {
    #         "password": forms.PasswordInput(),
    #     }
    pass
