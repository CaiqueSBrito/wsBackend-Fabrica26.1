from django.conf import settings
from django.urls import include, path
from . import views
from rest_framework import routers
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'pokebag', views.PokemonViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('pokemon/<uuid:id>/', views.pokemon_details, name='pokemon_details'),
    path('poke_list/', views.PokeAPIListView.as_view(), name='poke_list'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)