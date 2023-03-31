"""Dispensa_shared URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django_registration.backends.one_step.views import RegistrationView

from knox import views as knox_views

from core.views import IndexTemplateView 
from user.form import CustomUserForm
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #url to register via browser
    #bloccato, non si devono poter aggiungere account da browser
    path('accounts/register/', 
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url='/'
        ), name='django_registration_register'),
    path('accounts/register/', IndexTemplateView.as_view(), name='index'),

    #reset della password custom
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),      

    path('accounts/', include('django_registration.backends.one_step.urls')),

    #url to login via browser
    path('accounts/', include('django.contrib.auth.urls')),

    #url to user api
    path('api/', include('user.api.urls')),

    #url to login via browser api
    path('api-auth/', include('rest_framework.urls')),

    #url to login via API
    path(r'api/auth/', include('user.api.urls')),

    re_path(r'^.*$', IndexTemplateView.as_view(), name='index'),
]
