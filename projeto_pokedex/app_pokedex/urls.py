from django.conf import settings
from django.urls import include, path
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'pokebag', views.PokemonViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('pokemon/<uuid:id>/', views.pokemon_details, name='pokemon_details'),
    path('poke_list/', views.PokeAPIListView.as_view(), name='poke_list'),    
    path('pokemons/', views.pokemons_list, name='pokemons_list'),
    path('pokemons/<int:pokemon_id>/', views.poke_detail, name='poke_detail'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.entrar, name='login'),
    path('logout/', views.sair, name='logout'),
    path('api/token/', obtain_auth_token, name='api_token'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)