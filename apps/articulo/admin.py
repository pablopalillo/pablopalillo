from django.contrib import admin
from .models import Arcticulo, EstadoArticulo, TipoArticulo

class ArcticuloAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date')


admin.site.register(Arcticulo)
