from rest_framework import serializers
from dispense.models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi

#singola dispensa con tutti i suoi campi
class DispensaSerializer(serializers.ModelSerializer):

    inserito_da_dispensa = serializers.CharField(read_only=True)

    class Meta:
        model = Dispensa
        fields = '__all__'


