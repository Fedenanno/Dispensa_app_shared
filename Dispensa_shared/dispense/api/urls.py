from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as vw

#router = DefaultRouter()

urlpatterns = [
    #path per l'API /dispense/
    path('dispense/<int:id_dispensa>', vw.DispensaViewSet.as_view({'get': 'list', 'put': 'update', 'delete' : 'destroy'}), name='dispense'),
    path('dispense/', vw.DispensaViewSetList.as_view({'get': 'list', 'post': 'create'}) , name='dispense_list'),

    #path per l'API /dispense/shared/
    path('dispense/shared/<int:id_dispensa>', vw.DispensaShareViewSet.as_view({'post': 'create', 'put': 'update', 'delete' : 'destroy'}), name='dispense_shared'),

    #path per l'API /dispense/categorie/
    path('dispense/categorie/<int:id_dispensa>', vw.CategorieViewSet.as_view({'get': 'list', 'post': 'create', }), name='dispense_categorie'),
    path('dispense/categorie/<int:id_dispensa>/<int:id_categoria>', vw.CategorieViewSetId.as_view({'get': 'list', 'put': 'update', 'delete' : 'destroy'}), name='dispense_categorie'),

]