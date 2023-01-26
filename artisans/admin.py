import imp
from django.contrib import admin
from .models import Artisan, ArtisanInfo

# Register your models here.
admin.site.register(Artisan)
admin.site.register(ArtisanInfo)