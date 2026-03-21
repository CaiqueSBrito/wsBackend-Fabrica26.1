from django import forms

class PokemonForm(forms.Form):
    name = forms.CharField(max_length=100)
    sprites = forms.ImageField()
    type1 = forms.CharField(max_length=10)
    type2 = forms.CharField(max_length=10, required=False)
    hp = forms.IntegerField()
    attack = forms.IntegerField()
    defense = forms.IntegerField()
    speed = forms.IntegerField()
    abilites = forms.CharField(widget=forms.Textarea)