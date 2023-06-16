from django.urls import path, include

from knox.views import LogoutView, LogoutAllView

from user.api.views import CustomUserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('user/', CustomUserAPIView.as_view(), name='current-user'),

    #usati da knox
    path('', include('knox.urls')),
    path(r'register', RegisterAPIView.as_view()),
    path(r'login', LoginAPIView.as_view()),
    path(r'logout', LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall', LogoutAllView.as_view(), name='knox_logoutall')
]