from django.shortcuts import render, redirect
from .models import Lekcije, Video
from django.db.models import Q
from .forms import UcenikForm, IzborNastaveForm
from django.contrib import messages


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


def lekcije_godine(request, godina):
    lekcije = Lekcije.objects.all().filter(godina=godina)
    video = Video.objects.all().filter(godina=godina)
    lekcije_videi = lekcije.union(video).order_by('-vreme_posta')
    return render(request, "lekcije/lekcije_godine.html", {'lekcije': lekcije_videi, })


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


def prvi_razred_prijava(request):
    if request.method == 'POST':
        form = IzborNastaveForm(request.POST)
        if form.is_valid():
            ime = form.cleaned_data['ime']
            prezime = form.cleaned_data['prezime']
            messages.success(
                request, f'Učenik "{ime} {prezime}" se uspešno prijavio! ')
            form.save()
            return redirect('lekcije-home')
    else:
        form = UcenikForm()
    return render(request, 'lekcije/prvi_razred_prijava.html', {'form': form})


def izbor_nastave(request):
    if request.method == 'POST':
        form = IzborNastaveForm(request.POST)
        if form.is_valid():
            roditelj = form.cleaned_data['ime_prezime_roditelja']
            messages.success(
                request, f' "{roditelj} " je uspešno popunio obrazac! ')
            form.save()
            return redirect('lekcije-home')
    else:
        form = IzborNastaveForm()
    return render(request, 'lekcije/izbor_nastave.html', {'form': form})
