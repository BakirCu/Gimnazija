from django import forms
from .models import Ucenik
from django.forms import Select


class UcenikForm(forms.ModelForm):

    class Meta:
        model = Ucenik
        fields = ['id', 'ime', 'prezime', 'maticni_broj',
                  'jezik_na_kojem_se_odvija_nastava', 'prvi_strani_jezik', 'drugi_strani_jezik', 'smer', 'izborni_predmet',
                  'prvi_izborni_program', 'drugi_izborni_program']
        widgets = {
            'smer': Select(attrs={"onChange": 'myFunction()'})
        }
