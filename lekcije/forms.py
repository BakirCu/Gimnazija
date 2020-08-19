from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Ucenik, IzborNastave
from django.forms import Select, RadioSelect


class UcenikForm(forms.ModelForm):

    class Meta:
        model = Ucenik
        fields = ['id', 'ime', 'prezime', 'maticni_broj',
                  'jezik_na_kojem_se_odvija_nastava', 'prvi_strani_jezik', 'drugi_strani_jezik', 'smer', 'izborni_predmet',
                  'prvi_izborni_program', 'drugi_izborni_program']
        widgets = {
            'smer': Select(attrs={"onChange": 'myFunction()'})
        }


class IzborNastaveForm(forms.ModelForm):

    class Meta:
        IZBOR = (
            ("Da", "Da"), ("Ne", "Ne")
        )
        model = IzborNastave
        fields = ['ime_prezime_ucenika', 'odeljenje',
                  'izbor', 'ime_prezime_roditelja']
        labels = {
            "izbor": "Izjašnjavam se da će moje dete u septembru mesecu nastavu pratiti kombinovano:  jedne nedelje u školi - jedne nedelje od kuće onlajn"
        }
        widgets = {
            'izbor': RadioSelect(choices=IZBOR),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': " Vec ste jednom uspesno obavili prijavu, 'Hvala'",
            }
        }
