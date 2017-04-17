from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from .views import index
from . import views

urlpatterns = patterns('',
    url(r'^$', views.getArticle ),
    url(r'^(?P<article_id>\d{4})/$', views.getArticle),
    #url(r'^inicio2$', 'apps.general.views.indexSimple'),
    #url(r'^inicio/$', index2.as_view() ),
#    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'general/index.html'}, name='login'),
#    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
