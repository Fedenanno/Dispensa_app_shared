from rest_framework import serializers
from dispense.models import Dispensa, DispensaUser, Categorie, Prodotti, Elementi
from user.api.serializers import CustomUserSerializer

#-------- Dispensa --------
class DispensaSerializer(serializers.ModelSerializer):

    inserito_da = serializers.CharField(read_only=True)  #CustomUserSerializer(read_only=True)
    #In questo modo gli utenti non possono essere modificati
    # user = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Dispensa
        exclude = ['user']
        read_only_fields = ['users']

    def get_inserito_da(self, obj):
        return obj.inserito_da.username
    
    def get_user(self, obj):
        return obj.user.username
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        
        utenti = DispensaUser.objects.filter(id_dispensa=instance.id_dispensa)
        user_data = [{'user': utente.id_user.username, 'admin': utente.admin} for utente in utenti]
        
        ret['users'] = user_data
        
        return ret
        

class DispensaUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispensaUser
        fields = '__all__'

class DispensaUserSharedSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='id_user.username')  # Assicurati che il campo abbia lo stesso nome dell'attributo nel modello

    class Meta:
        model = DispensaUser
        fields = ['username']

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
    #Mostra il nome della categoria
    id_categoria = serializers.CharField(source='id_categoria.nome_categoria', read_only=True)
        
    class Meta:
        model = Prodotti
        fields = '__all__'
        
    def get_inserito_da(self, obj):
        return obj.inserito_da.username
    
    def get_id_categoria(self, obj):
        return obj.id_categoria.nome_categoria

    
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
    

