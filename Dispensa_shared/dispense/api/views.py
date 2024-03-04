from django.db import IntegrityError
from django.http import HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser



from user.models import CustomUser

from . import exceptions as exc
from .permissions import DispensaIsShared, DispensaIsAdmin, DispensaIsSharedOrOwner, DispensaIsOwnerOrOnlyDelete, DispensaIsOwner, ProdottoIsInDispensa
from dispense.models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi
from . import serializers as srz
from user.models import CustomUser as User

from .deamon import checkScadenze

#---------------Dispensa----------------
#restituisce una lista di tutte le dispense dell'utente o condivise con lui
#crea una nuova dispensa
class DispensaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = srz.DispensaSerializer
    pagination_class = None


    #restituisce:
    # default: tutte le dispense dell'utente o condivise con lui
    # owner = true: tutte le dispense dell'utente
    # owner = false: tutte le dispense condivise con lui
    def get_queryset(self):
        try:
            owner = self.request.query_params.get('owner')
            if owner == 'true':
                return Dispensa.objects.filter(inserito_da=self.request.user)
            elif owner == 'false':
                return Dispensa.objects.filter(id_dispensa__in=DispensaUser.objects.filter(id_user=self.request.user).exclude(condivisa_da=self.request.user).values_list('id_dispensa', flat=True))
        except:
            pass    
        return Dispensa.objects.filter(id_dispensa__in=DispensaUser.objects.filter(id_user=self.request.user).values_list('id_dispensa', flat=True))

    # crea una dipensa e la aggiunge alla tabella DispensaUser
    def perform_create(self, serializer):
        # aggiunge anche id_tabella e id_user alla tabella DispensaUser
        dispensa = serializer.save(inserito_da=self.request.user)
        DispensaUser.objects.create(
            id_dispensa=dispensa, id_user=self.request.user, condivisa_da=self.request.user)

#avendo un id_dispensa, restituisce la dispensa specificata, la aggiorna o la elimina (solo se è il proprietario)     
class DispensaViewSetId(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsOwner]
    serializer_class = srz.DispensaSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        return Dispensa.objects.filter(id_dispensa=self.kwargs['id_dispensa'])
    
    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        dispensa = self.kwargs['id_dispensa']
        user = self.request.user

        # controlla che l'utente che fa la richiesta sia chi ha creato la dipsensa
        if Dispensa.objects.get(id_dispensa=dispensa).inserito_da == user:
            # rimuove la entry con id_dispensa e id_user specificati dalla tabella DispensaUser e dalla tabella Dispensa
            if Dispensa.objects.filter(id_dispensa=dispensa).delete() and DispensaUser.objects.filter(id_dispensa=dispensa, id_user=user).delete():
                return Response("dispensa eliminata con successo", status.HTTP_200_OK)
            else:
                return Response("eliminazione dispensa fallita", status.HTTP_400_BAD_REQUEST)
        # se l'utente non è admin o non ha creato la dispensa, prova a togliere la condivisione
        else:
            raise exc.UserIsNotOwner()



# # view che in base al query params list, se true restituisce tutte le dispense che l'utente ha nella tabella DispensaUser, altrimenti solo la dispensa specificata dall'id nel query params id_dispensa
# class DispensaViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated, DispensaIsShared]
#     serializer_class = srz.DispensaSerializer
#     queryset = Dispensa.objects.all()
#     # rimuove la paginazione dei risultati, non è necessaria per questa tipologia di dati
#     pagination_class = None
#     lookup_field = 'id_dispensa'

#     def get_queryset(self):

#         dispensa = self.kwargs['id_dispensa']

#         # DEPRECATED ho inserito questo permesso a livello globale
#         # controlla che la dispensa sia condivisa con l'utente che fa la richiesta
#         # ds = DispensaUser.objects.filter(id_user=user, id_dispensa=dispensa)
#         # if not ds.exists():
#         #     raise UserHasNoPermission()

#         # ritorna la dispensa specificata dall'id nel query params id_dispensa
#         return Dispensa.objects.filter(id_dispensa=dispensa)

#     # aggiorna una dispensa con i dati passati nel body della richiesta
#     def perform_update(self, serializer):
#         # data = self.request.data
#         serializer.save()

#     # la delete usa il query params id_dispensa per identificare la dispensa da eliminare
#     def destroy(self, request, *args, **kwargs):
#         dispensa = self.kwargs['id_dispensa']
#         user = self.request.user

#         # controlla che l'utente che fa la richiesta sia chi ha creato la dipsensa
#         if Dispensa.objects.get(id_dispensa=dispensa).inserito_da == user:
#             # rimuove la entry con id_dispensa e id_user specificati dalla tabella DispensaUser e dalla tabella Dispensa
#             if Dispensa.objects.filter(id_dispensa=dispensa).delete() and DispensaUser.objects.filter(id_dispensa=dispensa, id_user=user).delete():
#                 return Response("dispensa eliminata con successo", status.HTTP_200_OK)
#             else:
#                 return Response("eliminazione dispensa fallita", status.HTTP_400_BAD_REQUEST)
#         # se l'utente non è admin o non ha creato la dispensa, prova a togliere la condivisione
#         else:
#             raise exc.UserIsNotOwner()

# # view per il parametro list


# class DispensaViewSetList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = srz.DispensaSerializer
#     queryset = Dispensa.objects.all()
#     # rimuove la paginazione dei risultati, non è necessaria per questa tipologia di dati
#     pagination_class = None
#     lookup_field = 'id_dispensa'

#     def get_queryset(self):
#         user = self.request.user
#         list = self.request.query_params.get('list')
#         owner = self.request.query_params.get('owner')

#         if list == 'true':
#             if not owner == None:
#                 if owner == 'true':
#                     # ritorna tutte le dispense create dall'utente
#                     return Dispensa.objects.filter(inserito_da=user)
#                 elif owner == 'false':
#                     # ritorna tutte le dispense condivise con l'utente ma che non sono state create dall'utente
#                     return Dispensa.objects.filter(id_dispensa__in=DispensaUser.objects.filter(id_user=user).exclude(condivisa_da=user).values_list('id_dispensa', flat=True))
#             # se il campo owner non è presente ritorna tutte le dispense dell'utente
#             else:
#                 return Dispensa.objects.filter(id_dispensa__in=DispensaUser.objects.filter(id_user=user).values_list('id_dispensa', flat=True))

#     # crea una dipensa e la aggiunge alla tabella DispensaUser
#     def perform_create(self, serializer):
#         # aggiunge anche id_tabella e id_user alla tabella DispensaUser
#         dispensa = serializer.save(inserito_da=self.request.user)
#         DispensaUser.objects.create(
#             id_dispensa=dispensa, id_user=self.request.user, condivisa_da=self.request.user)


# aggiunge o rimuove una dispensa presa dal path params id_dispensa e un user preso dalla richiesta alla tabella DispensaUser
class DispensaUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = srz.DispensaUserSerializer
    # rimuove la paginazione dei risultati, non è necessaria per questa tipologia di dati
    pagination_class = None

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# view per modificare le dispense condivise. POST aggiunge una dipsensa alla lista delle dispense condivise impostano il campo Dispensa.condivisa a true,
# DELETE la rimuove, se invece è il proprietario fa una DELETE restituisce un errore

def isShared(user, dispensa):
    try:
        DispensaUser.objects.get(id_dispensa=dispensa, id_user=user)
        return True
    except:
        return False

#TEST: OK
class DispensaShareViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsOwnerOrOnlyDelete]
    serializer_class = srz.DispensaUserSharedSerializer
    pagination_class = None
    #queryset = DispensaUser.objects.all()
    lookup_field = "id_dispensa"

    # TEST: OK
    # aggiunge una dispensa alla lista delle dispense condivise impostano il campo Dispensa.condivisa a true
    def perform_create(self, serializer):
        # campi necessari per arrivare fino a qui
        user = self.request.user
        dispensa = self.kwargs['id_dispensa']
        # campo gia controllato dal serializer
        new_user = self.request.data['username']
        admin_p = self.request.query_params.get('admin')
        if not new_user:
            return Response("Utente non specificato, campo <username> obbligatorio", status.HTTP_400_BAD_REQUEST)

        if not User.objects.filter(username=new_user).exists():
            raise exc.UserNotFound()
        
        new_user = User.objects.get(username=new_user).id
                

        # controlla che la dispensa non sia già condivisa con l'utente
        if isShared(new_user, dispensa):
            raise exc.DispensaAlreadyShared()

        try:
            dispensa_obj = Dispensa.objects.get(id_dispensa=dispensa)
            # trasforma il nome utente in id utente
            new_user = CustomUser.objects.get(id=new_user)  # (username=new_user).id
        except Dispensa.DoesNotExist:
            raise exc.DispensaNotFound()
        except CustomUser.DoesNotExist:
            raise exc.UserNotFound()
        
        
        # controlla che l'utente che fa la richiesta non sia lo stesso con cui condividere la dispensa
        if new_user == user:
            raise exc.SameUser()

        # crea una entry con id_dispensa e new_user specificati nella tabella DispensaUser
        try:
            serializer.save(id_dispensa=dispensa_obj, id_user=new_user, condivisa_da=user)

            #imposta il nuovo utente come admin della dispensa
            if admin_p == 'true':
                DispensaUser.objects.filter(id_dispensa=dispensa, id_user=new_user).update(admin=True)

            # imposta il campo condivisa a true
            Dispensa.objects.filter(id_dispensa=dispensa).update(condivisa=True)
            return Response("Dispensa condivisa con: "+new_user.username, status.HTTP_200_OK)
        except:
            return Response("Condivisione dispensa fallita", status.HTTP_400_BAD_REQUEST)

    #TEST: OK
    def update(self, serializer, pk="id_dispensa", *args, **kwargs):
        user = self.request.user
        dispensa = self.kwargs['id_dispensa']
        new_user = self.request.data['username']
        admin_p = self.request.query_params.get('admin')

        if not new_user:
            return Response("Utente non specificato, campo <username> obbligatorio", status.HTTP_400_BAD_REQUEST)

        if not User.objects.filter(username=new_user).exists():
            raise exc.UserNotFound()
        
        new_user = User.objects.get(username=new_user).id

        #controlla che chi fa la richiesta sia il proprietario della dispensa
        if Dispensa.objects.get(id_dispensa=dispensa).inserito_da == user:
            if admin_p == 'true':
                DispensaUser.objects.filter(id_dispensa=dispensa, id_user=new_user).update(admin=True)
                return Response("Utente impostato admin", status.HTTP_200_OK)            
            elif admin_p == 'false':
                DispensaUser.objects.filter(id_dispensa=dispensa, id_user=new_user).update(admin=False)
                return Response("Utente tolto admin", status.HTTP_200_OK)
            else:
                raise exc.QueryParamsAdminDispensaNotFound()

    # rimuove una dispensa dalla lista delle dispense condivise impostano.
    # se l'utente che fa la richiesta è il proprietario, rimuove tutte le occorrenze di quella dispensa da DispensaUser e imposta il campo condivisa a false

    #TEST: OK TODO cambiare id_user da payload a query params
    def destroy(self, serializer, pk="id_dispensa", *args, **kwargs):
        user = self.request.user
        dispensa = self.kwargs['id_dispensa']
        new_user = self.request.data['username']

        # controlla che l'utente che fa la richiesta sia chi ha creato la dipsensa (proprietario)
        if Dispensa.objects.get(id_dispensa=dispensa).inserito_da == user:
            #se viene passato il payload con l'id dell'utente da rimuovere
            print(new_user)
            if new_user:
                try:
                    if not User.objects.filter(username=new_user).exists():
                        raise exc.UserNotFound()

                    new_user = User.objects.get(username=new_user)
                    new_user_id = new_user.id
                    new_user_username = new_user.username
                    if not DispensaUser.objects.filter(id_dispensa=dispensa, id_user=new_user_id).exists():
                        raise exc.UserNotFound()

                    #Se l'utente che fa la richiesta e quello che l ha creata non puo essere rimosso
                    creat_disp = Dispensa.objects.get(id_dispensa=dispensa).inserito_da

                    if str(creat_disp) == str(new_user_username):
                        return Response("Non puoi rimuovere l'utente che ha creato la dispensa", status.HTTP_400_BAD_REQUEST)

                    DispensaUser.objects.filter(id_dispensa=dispensa, id_user=new_user_id).delete()
                    return Response("Dispensa non piu condivisa con l'utente", status.HTTP_200_OK)
                    
                except:
                    return Response("rimozione utente fallita, riprova piu tardi", status.HTTP_400_BAD_REQUEST)
    
            # altrimenti, rimuove tutte le entry con id_dispensa specificato dalla tabella DispensaUser tranne quella dove id_user = id_user
            try:
                DispensaUser.objects.filter(id_dispensa=dispensa).exclude(id_user=user).delete()
                # imposta il campo condivisa a false
                Dispensa.objects.filter(id_dispensa=dispensa).update(condivisa=False)
                return Response("Dispensa non piu condivisa, tutti gli accessi esterni di altri utenti sono stati rimossi", status.HTTP_200_OK)
            except:
                return Response("rimozione dispensa condivisa fallita, riprova piu tardi", status.HTTP_400_BAD_REQUEST)
        # se l'utente non è admin o non ha creato la dispensa, prova a togliere la condivisione
        else:
            
            # rimuove la entry con id_dispensa e id_user specificati dalla tabella DispensaUser
            if DispensaUser.objects.filter(id_dispensa=dispensa, id_user=user).delete():
                return Response("dispensa rimossa dalla propria lista con successo", status.HTTP_200_OK)
            else:
                return Response("rimozione dispensa condivisa fallita", status.HTTP_400_BAD_REQUEST)


# ---------- Categoria ------------
# se l'utente è admin (o propietario) puo inserire, modificare e cancellare le categorie
# se l'utente non è admin può solo vedere le categorie
def isAdmin(self):
    return DispensaUser.objects.filter(id_dispensa=self.kwargs['id_dispensa'], id_user=self.request.user, admin=True).exists() or Dispensa.objects.get(id_dispensa=self.kwargs['id_dispensa']).inserito_da == self.request.user

def sameDispensa(self):
        return int(self.request.data['id_dispensa']) == int(self.kwargs['id_dispensa'])
    
class CategorieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsShared]
    serializer_class = srz.CategorieSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'
    

    def get_queryset(self):
        return Categorie.objects.filter(id_dispensa=self.kwargs['id_dispensa']).order_by('nome_categoria')
    
    def perform_create(self, serializer):
        
        if isAdmin(self):
            if not sameDispensa(self):
                raise exc.UserHasNoPermission()
            try: 
                serializer.save(id_dispensa=Dispensa.objects.get(id_dispensa=self.kwargs['id_dispensa']), inserito_da=self.request.user)
                return Response("Categoria creata con successo", status.HTTP_200_OK)
            except:
                raise exc.CategoriaAlreadyExists()
        raise exc.UserIsNotAdmin()
    

class CategorieViewSetId(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsShared]
    serializer_class = srz.CategorieSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        return Categorie.objects.filter(id_dispensa=self.kwargs['id_dispensa'], id_categoria=self.kwargs['id_categoria'])
    
    def perform_update(self, serializer):
        if isAdmin(self):
            if not sameDispensa(self):
                raise exc.UserHasNoPermission()
            serializer.save(id_dispensa=Dispensa.objects.get(id_dispensa=self.kwargs['id_dispensa']))
            return Response("Categoria modificata con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
    def destroy(self, serializer, pk="id_categoria", *args, **kwargs):
        if isAdmin(self):
            Categorie.objects.filter(id_categoria=self.kwargs['id_categoria']).delete()
            return Response("Categoria eliminata con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()


# ---------- Prodotto ------------
# se l'utente è admin (o propietario) puo inserire, modificare e cancellare i prodotti
# se l'utente non è admin può solo vedere i prodotti

#funzione che controlla se l'id_Categoria del payload fa parte della dispensa con id specificato da id_dispensa nel url
def checkCategoria(self):
    return Categorie.objects.filter(id_dispensa=self.kwargs['id_dispensa'], id_categoria=self.request.data['id_categoria']).exists()

class ProdottiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsShared]
    serializer_class = srz.ProdottiSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        return Prodotti.objects.filter(id_dispensa=self.kwargs['id_dispensa']).order_by('nome_prodotto')
    
    def perform_create(self, serializer):
        if isAdmin(self):
            if not sameDispensa(self):
                print("Utente non admin")
                raise exc.UserHasNoPermission()
            if not checkCategoria(self):
                print("Categoria non trovata")
                raise exc.CategoriaNotFound()
            serializer.save(id_dispensa=Dispensa.objects.get(id_dispensa=self.kwargs['id_dispensa']), inserito_da=self.request.user)
            return Response("Prodotto creato con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
class ProdottiViewSetId(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsShared]
    serializer_class = srz.ProdottiSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        #return Prodotti.objects.filter(id_dispensa=self.kwargs['id_dispensa'], id_prodotto=self.kwargs['id_prodotto'])
        #in questo modo se non trova il prodotto restituisce 404
        #return get_object_or_404(Prodotti, id_dispensa=self.kwargs['id_dispensa'], id_prodotto=self.kwargs['id_prodotto'])
        prd = Prodotti.objects.filter(id_dispensa=self.kwargs['id_dispensa'], id_prodotto=self.kwargs['id_prodotto'])
        if prd.exists():
            return prd
        else:
            raise exc.ProdottoNotFound()

        

    def perform_update(self, serializer):
        if isAdmin(self):
            if not sameDispensa(self) or not checkCategoria(self):
                raise exc.UserHasNoPermission()
            serializer.save(id_dispensa=Dispensa.objects.get(id_dispensa=self.kwargs['id_dispensa']))
            return Response("Prodotto modificato con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
    def destroy(self, serializer, pk="id_prodotto", *args, **kwargs):
        if isAdmin(self):
            Prodotti.objects.filter(id_prodotto=self.kwargs['id_prodotto']).delete()
            return Response("Prodotto eliminato con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
class ProdottiListName(generics.ListAPIView):
    permission_classes = [IsAuthenticated, DispensaIsShared]
    serializer_class = srz.ProdottiSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        return Prodotti.objects.filter(id_dispensa=self.kwargs['id_dispensa'], nome_prodotto__contains=self.kwargs['nome_prodotto']).order_by('nome_prodotto')
    
# ---------- Elementi ------------

# se l'utente è admin (o propietario) puo inserire, modificare e cancellare gli elementi
# se l'utente non è admin può solo vedere gli elementi
# testare i controlli:
# Attuali: l'utente ha accesso alla dispensa, il prodotto fa parte della dispensa,
class ElementiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsShared, ProdottoIsInDispensa]
    serializer_class = srz.ElementiSerializer
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        data = None
        data2 = None
        try:
            data = self.request.query_params['data']
            data2 = self.request.query_params['data2']
        except:
            pass
        if data is not None and data2 is not None:
            return Elementi.objects.filter(id_prodotto=self.kwargs['id_prodotto'], data_scadenza__range=[data, data2]).order_by('data_scadenza')
        elif data is not None:
            return Elementi.objects.filter(id_prodotto=self.kwargs['id_prodotto'], data_scadenza__gte=data).order_by('data_scadenza')
        return Elementi.objects.filter(id_prodotto=self.kwargs['id_prodotto']).order_by('id_elemento')
    
    def perform_create(self, serializer):
        if isAdmin(self):
            serializer.save(id_prodotto=Prodotti.objects.get(id_prodotto=self.kwargs['id_prodotto']) ,inserito_da=self.request.user)
            return Response("Elemento creato con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
class ElementiViewSetId(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DispensaIsShared, ProdottoIsInDispensa]
    serializer_class = srz.ElementiSerializerEdit
    pagination_class = None
    lookup_field = 'id_prodotto'

    def get_queryset(self):
        return Elementi.objects.filter(id_prodotto=self.kwargs['id_prodotto'], id_elemento=self.kwargs['id_elemento'])
    
    def perform_update(self, serializer):
        if isAdmin(self):
            serializer.save(id_prodotto=Prodotti.objects.get(id_prodotto=self.kwargs['id_prodotto']))
            return Response("Elemento modificato con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
    def destroy(self, serializer, pk="id_elemento", *args, **kwargs):
        if isAdmin(self):
            Elementi.objects.filter(id_elemento=self.kwargs['id_elemento']).delete()
            return Response("Elemento eliminato con successo", status.HTTP_200_OK)
        raise exc.UserIsNotAdmin()
    
#view che restituisce tutti gli elementi che hanno una data di scadenza uguale a quella fornita nel query params data_scadenza.
#Cerca solo tra gli elementi sono figli di prodotti che fanno parte della dispensa specificata da id_dispensa, Elementi non ha il campo id_dispensa, lo ha il prodotto padre

class ElementiListDate(generics.ListAPIView):
    permission_classes = [IsAuthenticated, DispensaIsSharedOrOwner]
    serializer_class = srz.ElementiSerializerConProdotto
    pagination_class = None
    lookup_field = 'id_dispensa'

    def get_queryset(self):
        return Elementi.objects.filter(id_prodotto__in=Prodotti.objects.filter(id_dispensa=self.kwargs['id_dispensa']), data_scadenza=self.kwargs['data_scadenza']).order_by('data_scadenza')
    

        



#view che fa partire la funzione checkDispense
class MailDeamon(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = srz.ElementiSerializer
    

    def get_queryset(self):
        print("FUNZIONE CHECK DISPENSE: ")
        checkScadenze()
        return Elementi.objects.filter(id_elemento="-1")