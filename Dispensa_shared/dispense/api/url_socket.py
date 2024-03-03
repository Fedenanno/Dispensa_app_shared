from django.urls import path, include, re_path

from .consumers import UserShareConsumer

urlpatterns = [
    #Socket - notification
    re_path(r'ws/notifications/(?P<id_user>\w+)/$', UserShareConsumer.as_asgi()),
]