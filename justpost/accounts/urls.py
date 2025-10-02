from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/new/', views.UserCreateView.as_view(), name='new'),
    path('accounts/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    # Password change
    path('accounts/password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change_form.html',
            success_url='/accounts/password_change/done/'
        ), 
        name='password_change'
    ),
    path('accounts/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'
        ), 
        name='password_change_done'
    ),
]
