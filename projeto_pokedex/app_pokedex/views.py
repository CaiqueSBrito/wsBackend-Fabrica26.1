import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import PokemonSerializer

def home(request):
    return render(request, 'home.html')

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer