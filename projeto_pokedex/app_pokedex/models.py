from django.db import models
from django.contrib.auth.models import User
import uuid



class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemons')
    name = models.CharField(max_length=100)
    sprites = models.TextField(null=True, blank=True)
    sprite_img = models.ImageField(upload_to='sprites/', null=True, blank=True)
    type1 = models.CharField(max_length=11)
    type2 = models.CharField(max_length=10, blank=True, null=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    abilities = models.TextField()