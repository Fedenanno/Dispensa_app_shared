from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as vw

#router = DefaultRouter()

urlpatterns = [
    #path per la view DispensaViewSet che accetta i due query params list e id_dispensa facoltativi
    path('dispense/', vw.DispensaViewSet.as_view({'get': 'list', 'post': 'create'}), name='dispense'),

]