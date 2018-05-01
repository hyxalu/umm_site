from django.contrib import admin

# Register your models here.

from .models import Song
from .models import Evenement

admin.site.register(Song)
admin.site.register(Evenement)