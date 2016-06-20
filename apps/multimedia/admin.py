from django.contrib import admin
from .models import Multimedia


class MultimediaAdmin(admin.ModelAdmin):

    list_display    = ['titulo','descripcion']

admin.site.register(Multimedia, MultimediaAdmin)
