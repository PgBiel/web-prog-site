from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, SignupForm

# Create your views here.

class UserCreateView(CreateView):
    """User registration view"""
    model = User
    form_class = SignupForm
    template_name = "accounts/signup_form.html"

    def get_success_url(self):
        return reverse_lazy('posts:post-list')

class UserLoginView(LoginView):
    """User login view"""
    next_page = "posts:post-list"
    template_name = "accounts/login.html"
    authentication_form = LoginForm

class UserLogoutView(LogoutView):
    """User logout view"""
    # next_page = "posts:post-list"
    template_name = "accounts/logout.html"
