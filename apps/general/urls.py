from django.conf.urls import patterns, include, url
from .views import indexSimple,index2

urlpatterns = patterns('',
    url(r'^inicio2$', 'apps.general.views.indexSimple'),
    url(r'^inicio/$', index2.as_view() ),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'general/index.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
