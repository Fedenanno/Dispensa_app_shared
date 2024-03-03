"""
ASGI config for Dispensa_shared project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import dispense.api.url_socket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dispensa_shared.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': URLRouter(
      dispense.api.url_socket.urlpatterns
    ),
})
