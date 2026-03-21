from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):    
    id = serializers.UUIDField(read_only=True)
    sprite_img = serializers.ImageField(use_url=True, required=False)
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)
    
    def get_serializer_context(self):
        return {'request': self.request}

    class Meta:
        model = Pokemon
        fields = '__all__'

