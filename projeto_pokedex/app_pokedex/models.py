from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    sprites = models.ImageField(upload_to='sprites/')
    type1 = models.CharField(max_length=10, required=True)
    type2 = models.CharField(max_length=10, blank=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    abilites = models.TextField()