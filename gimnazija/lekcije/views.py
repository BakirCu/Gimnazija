from django.shortcuts import render


def home(request):
    return render(request, 'lekcije/home.html')
