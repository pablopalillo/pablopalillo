from django.contrib import admin
from .models import Articulo

# Globally disable delete selected
admin.site.disable_action('delete_selected')


class ArcticuloAdmin(admin.ModelAdmin):

    list_display    = ['nombre','estado']

    class Media:
        js = ('/static/js/vendor/tinymce/tinymce.min.js','/static/js/admin.js')

    """
     queryset es el que controla el resultado del visor.
     trataremos de cambiar la consulta para mostrar solo los articulos
     publicados con changelist_view
    """

    def get_queryset(self, request):

        qs = super(ArcticuloAdmin, self).get_queryset(request)

        return qs.exclude(estado = 3)


    """
    actionCustomDelete : accion para modificar el comportamiento del Borrar acutal

    Params:     1.The current ModelAdmin
                2. An HttpRequest representing the current request,
                3. A QuerySet containing the set of objects selected by the user.
    """

    def actionCustomDelete(modeladmin, request, queryset):

        queryset.update(estado='3')

    actionCustomDelete.short_description = "Eliminar dato(s) seleccionados."
    actions         = ['actionCustomDelete']




admin.site.register(Articulo, ArcticuloAdmin)
