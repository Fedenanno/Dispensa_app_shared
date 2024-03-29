from rest_framework import permissions
from dispense.models import DispensaUser, Dispensa, Prodotti

#Puo avere accesso solo se l'utente è admin del sistema
class IsAdminOrDenied(permissions.BasePermission):

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # non consentiamo nemmeno la GET, HEAD o OPTIONS requests.
        return request.user.is_staff

#se esiste una riga con id_dispensa e id_user nella tabella DispensaUser allora la dispensa è condivisa, l'utente puo modificare la dispensa, altrimenti no
class DispensaIsShared(permissions.BasePermission):
    def has_permission(self, request, view):
        #controlla se l'id dello user che fa la richiesta è associato ad un id_dispensa nella tabella DispensaUser
        ds = DispensaUser.objects.filter(id_user=request.user, id_dispensa=view.kwargs['id_dispensa'])
        if ds.exists():
            return True
        return False
    
class DispensaIsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        #controlla se è proprietario, controllando il campo inserito_da_dispensa della tabella Dispensa
        d = Dispensa.objects.filter(id_dispensa=view.kwargs['id_dispensa'], inserito_da=request.user)
        if d.exists():
            return True
        
class DispensaIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        d = DispensaUser.objects.filter(id_dispensa=view.kwargs['id_dispensa'], user=request.user)
        if d.exists() and d.admin == True:
            return True
        
    
class DispensaIsOwnerOrOnlyDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        #controlla se è proprietario, controllando il campo inserito_da_dispensa della tabella Dispensa
        d = Dispensa.objects.filter(id_dispensa=view.kwargs['id_dispensa'], inserito_da=request.user)
        if d.exists():
            return True
        #se non è proprietario controlla se la richiesta è una delete
        if request.method == 'DELETE':
            return True
        return False
        
class DispensaIsSharedOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        #controlla se l'id dello user che fa la richiesta è associato ad un id_dispensa nella tabella DispensaUser
        ds = DispensaUser.objects.filter(id_user=request.user, id_dispensa=view.kwargs['id_dispensa'])
        if ds.exists() or request.user.is_staff:
            return True
        
        #se non è condivisa controlla se è proprietario, controllando il campo inserito_da_dispensa della tabella Dispensa
        d = Dispensa.objects.filter(id_dispensa=view.kwargs['id_dispensa'], inserito_da_dispensa=request.user)
        if d.exists():
            return True

#------- Prodotti -------
class ProdottoIsInDispensa(permissions.BasePermission):
    def has_permission(self, request, view):
        #controlla che l'id del prodotto è associato all'id della dispensa
        d = Prodotti.objects.filter(id_dispensa=view.kwargs['id_dispensa'], id_prodotto=view.kwargs['id_prodotto'])
        if d.exists():
            return True
        return False

#------- Categorie -------

        


# class IsOwnerOrShared(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.user or obj.shared_with == request.user