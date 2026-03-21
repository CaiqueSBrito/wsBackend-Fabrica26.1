import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import PokemonSerializer
from django.core.cache import cache as django_cache
from rest_framework.views import APIView
from rest_framework.response import Response

def home(request):
    return render(request, 'app_pokedex/home.html')

def pokemon_details(request, id):
    pokemon = Pokemon.objects.get(id=id)
    stats = {
        'hp': round(pokemon.hp / 255 * 100),
        'attack': round(pokemon.attack / 255 * 100),
        'defense': round(pokemon.defense / 255 * 100),
        'speed': round(pokemon.speed / 255 * 100),
    }
    return render(request, 'app_pokedex/pokemon_details.html', {'pokemon': pokemon, 'stats': stats})

class PokeAPIListView(APIView):
    def get(self, request):
        cache = django_cache.get('pokeapi_cache')
        if cache is None:
            data = requests.get('https://pokeapi.co/api/v2/pokemon?limit=2000')
            if data.status_code == 200:
                django_cache.set('pokeapi_cache', data.json(), timeout=60*60)
                return Response(data.json())
            else:
                return Response({'error': 'Falha ao buscar PokeAPI'}, status=502)
        else:
            return Response(cache)

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filterset_fields = ['type1', 'type2']
    search_fields = ['name']
    ordering_fields = ['hp', 'attack', 'defense', 'speed']
