from django.http import HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser



from .exceptions import QueryParamsIdDispensaNotFound, UserHasNoPermission
from .permissions import DispensaIsShared, DispensaIsAdmin, DispensaIsSharedOrAdmin
from dispense.models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi
from . import serializers as srz


#view che in base al query params list, se true restituisce tutte le dispense che l'utente ha nella tabella DispensaUser, altrimenti solo la dispensa specificata dall'id nel query params id_dispensa
class DispensaViewSet(viewsets.ModelViewSet):
    #permission_classes = (DispensaIsShared)
    serializer_class = srz.DispensaSerializer
    #rimuove la paginazione dei risultati, non è necessaria per questa tipologia di dati
    pagination_class = None


    def get_queryset(self):
        if self.request.query_params.get('list') == 'true':
            return Dispensa.objects.filter(id_dispensa__in=DispensaUser.objects.filter(id_user=self.request.user).values_list('id_dispensa', flat=True))
        else:
            #ritorna 400 se non è specificato l'id della dispensa
            if self.request.query_params.get('id_dispensa') == None:
                #ritorna 400 se non è specificato l'id della dispensa
                raise QueryParamsIdDispensaNotFound()
            
            #controlla che la dispensa sia condivisa con l'utente che fa la richiesta
            ds = DispensaUser.objects.filter(id_user=self.request.user, id_dispensa=self.request.query_params.get('id_dispensa'))
            if not ds.exists():
                raise UserHasNoPermission()
            
            #ritorna la dispensa specificata dall'id nel query params id_dispensa
            return Dispensa.objects.filter(id_dispensa=self.request.query_params.get('id_dispensa'))

    #crea una dipensa e la aggiunge alla tabella DispensaUser
    def perform_create(self, serializer):
        #aggiunge anche id_tabella e id_user alla tabella DispensaUser
        dispensa = serializer.save(inserito_da=self.request.user)
        DispensaUser.objects.create(id_dispensa=dispensa, id_user=self.request.user, condivisa_da=self.request.user)

    def perform_update(self, serializer):
        serializer.save(inserito_da=self.request.user)

    #la delete usa il query params id_dispensa per identificare la dispensa da eliminare
    def destroy(self, request, *args, **kwargs):
        if request.query_params.get('id_dispensa') == None:
            #ritorna 400 se non è specificato l'id della dispensa
            raise QueryParamsIdDispensaNotFound()
            #return Response("query params 'id_richiesta' necessario", status.HTTP_400_BAD_REQUEST)#HttpResponseBadRequest("query params 'id_dispensa' non specificato, per altre informazioni consultare la documentazione", status=400)
        DispensaIsAdmin.has_permission(self, self.request, self)
        return super().destroy(request, *args, **kwargs)
