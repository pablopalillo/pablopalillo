from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pablopalillo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))

    #general
#    url(r'^', include('apps.general.urls')),

    #Images
#    url(r'^image/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root' : settings.BASE_DIR+'/image/',} ),

    #productos
#    url(r'^productos/', include('apps.productos.urls')),

)
