import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import PokemonSerializer

def home(request):
    return render(request, 'home.html')

def pokemon_details(request, id):
    pokemon = Pokemon.objects.get(id=id)
    return render(request, 'pokemon_details.html', {'pokemon': pokemon})

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filterset_fields = ['type1', 'type2']
    search_fields = ['name']
    ordering_fields = ['hp', 'attack', 'defense', 'speed']
