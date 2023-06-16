from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as vw

#router = DefaultRouter()

urlpatterns = [
    #path per l'API /dispense/
    #?owner: true | false
    path('dispense/', vw.DispensaViewSet.as_view({'get': 'list', 'post': 'create'}), name='dispense'),
    path('dispense/<int:id_dispensa>/', vw.DispensaViewSetId.as_view({'get': 'list', 'put': 'update', 'delete' : 'destroy'}) , name='dispense_list'),

    #path per l'API /dispense/shared/
    #?admin: true | false
    path('dispense/<int:id_dispensa>/shared/', vw.DispensaShareViewSet.as_view({'post': 'create', 'put': 'update', 'delete' : 'destroy'}), name='dispense_shared'),

    #path per l'API /dispense/categorie/
    path('dispense/<int:id_dispensa>/categorie/', vw.CategorieViewSet.as_view({'get': 'list', 'post': 'create', }), name='dispense_categorie'),
    path('dispense/<int:id_dispensa>/categorie/<int:id_categoria>/', vw.CategorieViewSetId.as_view({'get': 'list', 'put': 'update', 'delete' : 'destroy'}), name='dispense_categorie_id'),

    #path per l'API /dispense/prodotti/
    path('dispense/<int:id_dispensa>/prodotti/', vw.ProdottiViewSet.as_view({'get': 'list', 'post': 'create', }), name='dispense_prodotti'),
    path('dispense/<int:id_dispensa>/prodotti/<int:id_prodotto>/', vw.ProdottiViewSetId.as_view({'get': 'list', 'put': 'update', 'delete' : 'destroy'}), name='dispense_prodotti_id'),
    path('dispense/<int:id_dispensa>/prodotti/<str:nome_prodotto>/', vw.ProdottiListName.as_view(), name='dispense_prodotti_name'),

    #path per l'API /dispense/elementi/
    #API che fornisce gli elementi in scadenza in un data specifica per una dispensa
    path('dispense/<int:id_dispensa>/prodotti/elementi/<data_scadenza>/', vw.ElementiListDate.as_view(), name='dispense_elementi'),
    #?data: YYYY-MM-DD 
    #?data2: YYYY-MM-DD (utilizzata per la ricerca di elementi compresi tra due date)
    path('dispense/<int:id_dispensa>/prodotti/<int:id_prodotto>/elementi/', vw.ElementiViewSet.as_view({'get': 'list', 'post': 'create', }), name='dispense_elementi'),
    path('dispense/<int:id_dispensa>/prodotti/<int:id_prodotto>/elementi/<int:id_elemento>/', vw.ElementiViewSetId.as_view({'get': 'list', 'put': 'update', 'delete' : 'destroy'}), name='dispense_elementi_id'),


    #Mail Deamon
    path('dispense/deamon/', vw.MailDeamon.as_view({'get' : 'list'}), name="dispense_mail_deamon"),
]