from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pablopalillo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #articulo
    url(r'^articulo/', include('apps.articulo.urls')),

    #home-main
    url(r'^$', include('apps.main.urls'))

    #general
#    url(r'^', include('apps.general.urls')),


    #productos
#    url(r'^productos/', include('apps.productos.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
