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
    # Password reset
    path('accounts/password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset_form.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.html',
            success_url='/accounts/password_reset/done/'
        ), 
        name='password_reset'
    ),
    path('accounts/password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path('accounts/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url='/accounts/reset/done/'
        ), 
        name='password_reset_confirm'
    ),
    path('accounts/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ), 
        name='password_reset_complete'
    ),
]
