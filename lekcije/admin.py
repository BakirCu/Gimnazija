from django.contrib import admin
from .models import Lekcije, Video


admin.site.register([Lekcije, Video])
