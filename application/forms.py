from .models import Games
from django.forms import ModelForm, TextInput, DateTimeInput

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = ['name', 'type', 'popularity', 'buy', 'date']

        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Game name...'}),
            "type": TextInput(attrs={'class': 'form-control', 'placeholder': 'Game type...'}),
            "popularity": TextInput(attrs={'class': 'form-control', 'placeholder': 'Popularity...'}),
            "buy": TextInput(attrs={'class': 'form-control', 'placeholder': 'Price...'}),
            "date": DateTimeInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Added time...'})
        }


# class UserForm(ModelForm):
#     class Meta:
#         model = User