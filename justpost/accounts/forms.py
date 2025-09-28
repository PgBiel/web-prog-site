from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from posts.models import Post


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }

class LoginForm(AuthenticationForm):
    # class Meta:
    #     model = User
    #     fields = ["username", "password"]
    #     widgets = {
    #         "password": forms.PasswordInput(),
    #     }
    pass
