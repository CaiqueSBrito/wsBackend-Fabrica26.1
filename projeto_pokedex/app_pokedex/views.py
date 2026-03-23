import asyncio
import httpx
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import PokemonSerializer
from django.core.cache import cache as django_cache
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token


def home(request):
    return render(request, 'app_pokedex/home.html')

def pokemons_list(request):
    return render(request, 'app_pokedex/pokemons_list.html')


import json

@ensure_csrf_cookie
def registro(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        email    = body.get('email')
        senha    = body.get('senha')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'erro': 'Email já cadastrado'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=senha)
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'ok': True, 'token': token.key})

    return render(request, 'app_pokedex/registro.html')

@ensure_csrf_cookie
def entrar(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body.get('email')
        senha = body.get('senha')

        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            return JsonResponse({'erro': 'Usuário não encontrado'}, status=400)

        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'ok': True, 'token': token.key})
        return JsonResponse({'erro': 'Senha incorreta'}, status=400)

    return render(request, 'app_pokedex/login.html')

def sair(request):
    logout(request)
    return redirect('login')


def poke_detail(request, pokemon_id):
    data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/').json()
    pokemon = {
        'name':      data['name'],
        'sprite_img': data['sprites']['front_default'],
        'type1':     data['types'][0]['type']['name'],
        'type2':     data['types'][1]['type']['name'] if len(data['types']) > 1 else '',
        'hp':        next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'hp'),
        'attack':    next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'attack'),
        'defense':   next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'defense'),
        'speed':     next(s['base_stat'] for s in data['stats'] if s['stat']['name'] == 'speed'),
        'abilities': ' '.join([a['ability']['name'] for a in data['abilities']]),
        'id':        data['id'],
    }
    return render(request, 'app_pokedex/poke_detail.html', {'pokemon': pokemon})

def pokemon_details(request, id):
    pokemon = Pokemon.objects.get(id=id)
    stats = {
        'hp':      round(pokemon.hp / 255 * 100),
        'attack':  round(pokemon.attack / 255 * 100),
        'defense': round(pokemon.defense / 255 * 100),
        'speed':   round(pokemon.speed / 255 * 100),
    }
    return render(request, 'app_pokedex/pokemon_details.html', {
        'pokemon': pokemon,
        'stats': stats,
        'sprite_url': pokemon.sprite_img.url if pokemon.sprite_img and pokemon.sprite_img.name else None
    })

class PokeAPIListView(APIView):
    def get(self, request):
        cache = django_cache.get('pokeapi_cache')
        if cache is None:
            resultado = asyncio.run(self._buscar_async())
            django_cache.set('pokeapi_cache', resultado, timeout=60*60)
            return Response(resultado)
        return Response(cache)

    async def _buscar_async(self, limit, offset):
        data = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}')
        urls = [p['url'] for p in data.json()['results']]
        count = data.json()['count']

        async with httpx.AsyncClient(timeout=30) as client:
            tasks = [client.get(url) for url in urls]
            respostas = await asyncio.gather(*tasks)

        pokemons = []
        for r in respostas:
            d = r.json()
            pokemons.append({
                'id':     d['id'],
                'name':   d['name'],
                'sprite': d['sprites']['front_default'],
                'types':  [t['type']['name'] for t in d['types']],
            })

        return {
            'count':   count,
            'results': pokemons
        }

    def get(self, request):
        limit  = int(request.query_params.get('limit', 20))
        offset = int(request.query_params.get('offset', 0))

        CACHE_KEY = f'pokeapi_{offset}_{limit}'
        cache = django_cache.get(CACHE_KEY)

        if cache is None:
            resultado = asyncio.run(self._buscar_async(limit, offset))
            django_cache.set(CACHE_KEY, resultado, timeout=60*60*24)
            return Response(resultado)

        return Response(cache)

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PokemonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filterset_fields = ['type1', 'type2']
    search_fields = ['name']
    ordering_fields = ['hp', 'attack', 'defense', 'speed']

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Pokemon.objects.filter(usuario=self.request.user)
        return Pokemon.objects.none()