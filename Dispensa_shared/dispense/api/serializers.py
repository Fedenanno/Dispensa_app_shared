from rest_framework import serializers
from dispense.models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi
from user.api.serializers import CustomUserSerializer

#-------- Dispensa --------
class DispensaSerializer(serializers.ModelSerializer):

    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)
    #In questo modo gli utenti non possono essere modificati
    user = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = Dispensa
        fields = '__all__'
        read_only_fields = ['user']

    def get_inserito_da(self, obj):
        return obj.inserito_da.username
    
    def get_user(self, obj):
        return obj.user.username

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

#-------- Prodotti --------
class ProdottiSerializer(serializers.ModelSerializer):
        
    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)
        
    class Meta:
        model = Prodotti
        fields = '__all__'
        
    def get_inserito_da(self, obj):
        return obj.inserito_da.username
    
class ProdottiSerializerSemplice(serializers.ModelSerializer):

    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)
        
    class Meta:
        model = Prodotti
        fields = ['id_prodotto', 'nome_prodotto', 'descrizione_prodotto', 'inserito_da']
        
    def get_inserito_da(self, obj):
        return obj.inserito_da.username
        
#-------- Elementi --------
class ElementiSerializer(serializers.ModelSerializer):
                    
    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)            
                    
    class Meta:
        model = Elementi
        fields = '__all__'
                
    def get_inserito_da(self, obj):
        return obj.inserito_da.username 

class ElementiSerializerEdit(serializers.ModelSerializer):
                    
    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)            
                    
    class Meta:
        model = Elementi
        fields = ['data_scadenza', 'inserito_da']
                
    def get_inserito_da(self, obj):
        return obj.inserito_da.username 
        
class ElementiSerializerConProdotto(serializers.ModelSerializer):

    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)
    id_prodotto = ProdottiSerializerSemplice(read_only=True)

    class Meta:
        model = Elementi
        fields = '__all__'

    def get_inserito_da(self, obj):
        return obj.inserito_da.username
    

