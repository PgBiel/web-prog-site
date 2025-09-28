from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/new/', views.UserCreateView.as_view(), name='new'),
    path('accounts/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
]
