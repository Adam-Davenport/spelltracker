from django import forms
from spelltracker.models import Character


class Character_Form(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }