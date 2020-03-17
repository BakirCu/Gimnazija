from django.shortcuts import render


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


def predmet(request, id):

    return render(request, 'lekcije/predmet.html')
