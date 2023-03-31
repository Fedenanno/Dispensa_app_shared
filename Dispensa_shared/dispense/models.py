from django.db import models


# Create your models here.

# class Categoria(models.Model):

#     codice_categoria = models.AutoField(primary_key=True, unique=True)
#     nome_categoria = models.CharField(max_length=50)
#     data_creazione = models.DateTimeField(auto_now_add=True)
#     data_modifica = models.DateTimeField(auto_now=True)
#     attiva = models.BooleanField(default=True)
#     inserito_da = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inserito_da')