from django.contrib import admin
from .models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi

# Register your models here.
admin.site.register(Dispensa)
admin.site.register(DispensaUser)
admin.site.register(Categorie)
admin.site.register(Prodotti)
admin.site.register(Elementi)

