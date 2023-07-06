from django.db import models
from django.conf import settings

#TODO !Important, toliere l'id come visibile e sostituirlo con un UUID casuale. In questo modo non si  
# espongono le informazioni sensibili

#Modelli per la web-app dispensa shared
class Dispensa(models.Model):
    #PK
    id_dispensa = models.AutoField(primary_key=True, unique=True)

    #da eliminare? tutte le politiche di m to n le sto implementando con i custom manualmente
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user', through='DispensaUser', through_fields=('id_dispensa', 'id_user'))

    nome_dispensa = models.CharField(max_length=50, blank=False, null=False)
    condivisa = models.BooleanField(default=False)
    attiva = models.BooleanField(default=True)
    data_ora_creazione = models.DateTimeField(auto_now_add=True)
    data_ora_modifica = models.DateTimeField(auto_now=True)
    inserito_da = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inserito_da_dispensa')

    class Meta:
        verbose_name = "Dispensa"
        verbose_name_plural = "Dispense"

    def __str__(self):
        return "id: {}, nome: {}".format(self.id_dispensa, self.nome_dispensa)


#custom through model: from Dispenta to User, form M to N relationship
class DispensaUser(models.Model):

    #PK
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='id_user_disp_user')
    id_dispensa = models.ForeignKey(Dispensa, on_delete=models.CASCADE, related_name='id_dispensa_disp_user')

    notifiche = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    condivisa_da = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='condivisa_da_disp_user', blank=False, null=False)

    class Meta:
        verbose_name = "DispensaUser"
        verbose_name_plural = "DispensaUsers"
        constraints = [
            models.UniqueConstraint(
                fields=['id_user', 'id_dispensa'], name='unique_disp_user'
            )
        ]

    def __str__(self):
        return "user: {}(id: {}), dispensa: {}(id: {})".format(self.id_user.username, self.id_user.id, self.id_dispensa.nome_dispensa, self.id_dispensa.id_dispensa)

class Categorie(models.Model):
    
    #PK
    id_dispensa = models.ForeignKey(Dispensa, on_delete=models.CASCADE, related_name='id_dispensa_categoria')
    id_categoria = models.AutoField(primary_key=True, unique=True)

    nome_categoria = models.CharField(max_length=50, blank=False, null=False)
    data_ora_creazione = models.DateTimeField(auto_now_add=True)
    data_ora_modifica = models.DateTimeField(auto_now=True)
    attiva = models.BooleanField(default=True)
    inserito_da = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inserito_da_categoria')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        constraints = [
            models.UniqueConstraint(
                fields=['id_dispensa', 'nome_categoria'], name='unique_categoria_dispensa'
            )
        ]
    
    def __str__(self):
        return "disp: {} cat: {} nome: {}".format(self.id_dispensa.id_dispensa, self.id_categoria, self.nome_categoria)
    
class Prodotti(models.Model):

    #PK
    id_prodotto = models.IntegerField(primary_key=True, unique=True)
    id_dispensa = models.ForeignKey(Dispensa, on_delete=models.CASCADE, related_name='id_dispensa_prodotto')
    
    id_categoria = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='id_categoria_prodotto', blank=True, null=True)

    nome_prodotto = models.CharField(max_length=50, blank=False, null=False)
    marca_prodotto = models.CharField(max_length=50, blank=True, null=True)
    descrizione_prodotto = models.CharField(max_length=200, blank=True, null=True)
    prezzo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    attivo = models.BooleanField(default=True)
    scadenza_default = models.IntegerField(blank=True, null=True)

    data_ora_creazione = models.DateTimeField(auto_now_add=True)
    data_ora_modifica = models.DateTimeField(auto_now=True)
    inserito_da = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inserito_da_prodotto', blank=False, null=False)

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"
        constraints = [
            models.UniqueConstraint(
                fields=['id_prodotto', 'id_dispensa'], name='unique_prodotto_dispensa'
            )
        ]
    
    def __str__(self):
        return "disp: {} prod: {} nome: {}".format(self.id_dispensa.id_dispensa, self.id_prodotto, self.nome_prodotto)

class Elementi(models.Model):

    #PK
    id_elemento = models.AutoField(primary_key=True, unique=True)

    data_scadenza = models.DateField(blank=False, null=False)
    id_prodotto = models.ForeignKey(Prodotti, on_delete=models.CASCADE, related_name='prodotto_elemento')

    data_ora_creazione = models.DateTimeField(auto_now_add=True)
    data_ora_modifica = models.DateTimeField(auto_now=True)
    inserito_da = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inserito_da_elemento', blank=False, null=False)

    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementi"

    def __str__(self):
        return "id: {} prd: {} scad: {}".format(self.id_elemento, self.id_prodotto.nome_prodotto, self.data_scadenza)

#multi primary key https://stackoverflow.com/questions/16800375/how-can-i-set-two-primary-key-fields-for-my-models-in-django