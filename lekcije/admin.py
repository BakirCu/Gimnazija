from django.contrib import admin
from .models import Lekcije, Video, Ucenik


admin.site.register([Lekcije, Video, Ucenik])
