from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    sprites = models.ImageField(upload_to='sprites/')
    type1 = models.CharField(max_length=10)
    type2 = models.CharField(max_length=10, blank=True, null=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    abilites = models.TextField()