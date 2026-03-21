from django.db import models
import uuid
# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
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