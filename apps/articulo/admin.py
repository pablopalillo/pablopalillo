from django.contrib import admin
from .models import Articulo

class ArcticuloAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/vendor/tinymce/tinymce.min.js','/static/js/admin.js')


admin.site.register(Articulo, ArcticuloAdmin)
