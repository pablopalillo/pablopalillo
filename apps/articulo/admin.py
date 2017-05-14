from django.contrib import admin
from .models import Articulo
from .models import Meta
from apps.multimedia.models import Articuloxmultimedia
from pprint import pprint

# Globally disable delete selected
admin.site.disable_action('delete_selected')
###
# TabularInline
# Permite generar un formulario con varios modelos relacionados,
###
class MultimediaInlineAdmin(admin.TabularInline):
    model = Articuloxmultimedia

    #readonly_fields = ('classifier', 'err_count')
    extra = 0

class MetaInlineAdmin(admin.TabularInline):
    model = Meta
    list_display    = ['metatype','metadata']

class ArcticuloAdmin(admin.ModelAdmin):
    inlines = [
        MultimediaInlineAdmin,
        MetaInlineAdmin
    ]
    list_display    = ['nombre','estado']
    prepopulated_fields = {"slug": ("nombre",)}

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
        art = request.POST['_selected_action']

        Meta.objects.filter(id_articulo = art).delete()
        queryset.update(estado='3')

    actionCustomDelete.short_description = "Eliminar dato(s) seleccionados."
    actions         = ['actionCustomDelete']

class MetaAdmin(admin.ModelAdmin):
    inlines = [
        MetaInlineAdmin,
    ]



admin.site.register(Articulo, ArcticuloAdmin)
