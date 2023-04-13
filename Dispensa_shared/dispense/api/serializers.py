from rest_framework import serializers
from dispense.models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi
from user.api.serializers import CustomUserSerializer

#-------- Dispensa --------
class DispensaSerializer(serializers.ModelSerializer):

    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)

    class Meta:
        model = Dispensa
        fields = '__all__'

    def get_inserito_da(self, obj):
        return obj.inserito_da.username

class DispensaUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispensaUser
        fields = '__all__'

class DispensaUserSharedSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispensaUser
        
        fields = ['id_user']

#-------- Categorie --------
class CategorieSerializer(serializers.ModelSerializer):
    
        inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)
    
        class Meta:
            model = Categorie
            fields = '__all__'
    
        def get_inserito_da(self, obj):
            return obj.inserito_da.username
