from django.contrib import admin
from .models import Lekcije, Video, Ucenik, IzborNastave


admin.site.register([Lekcije, Video, Ucenik, IzborNastave])
