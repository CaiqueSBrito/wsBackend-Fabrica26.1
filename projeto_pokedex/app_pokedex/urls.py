from django.conf import settings
from django.urls import include, path
from . import views
from rest_framework import routers
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)