from django.urls import path, include

from knox.views import LogoutView

from user.api.views import CustomUserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('user/', CustomUserAPIView.as_view(), name='current-user'),

    #usati da knox
    path('', include('knox.urls')),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]