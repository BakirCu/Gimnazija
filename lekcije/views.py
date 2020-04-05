from django.shortcuts import render
from .models import Lekcije, Video
from django.db.models import Q


def home(request):
    return render(request, 'lekcije/home.html')


def prvi_razred(request):

    return render(request, 'lekcije/prvi_razred.html')


def drugi_razred(request):
    return render(request, 'lekcije/drugi_razred.html')


def treci_razred(request):
    return render(request, 'lekcije/treci_razred.html')


def cetvrti_razred(request):
    return render(request, 'lekcije/cetvrti_razred.html')


def lekcija(request, id):
    lekcija = Lekcije.objects.get(id=int(id))
    return render(request, 'lekcije/lekcija.html', {'lekcija': lekcija, })


def video(request, id):

    video = Video.objects.get(id=int(id))
    return render(request, 'lekcije/video.html', {'video': video, })


def predmet(request, predmet, godina):

    lekcije = Lekcije.objects.all().filter(
        Q(predmet=predmet) & Q(godina=godina))
    video = Video.objects.all().filter(
        Q(predmet=predmet) & Q(godina=godina))
    lekcije_videi = lekcije.union(video).order_by('-vreme_posta')
    return render(request, 'lekcije/predmet.html', {'lekcije': lekcije_videi, })
