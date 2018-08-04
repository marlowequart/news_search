# coding: utf-8

from django.conf.urls import include, url

#enable the Django Admin: (recommended)
from django.contrib import admin
admin.autodiscover()

#import the function I want to call below
from services import views as url_views
#from services.views import *

urlpatterns = [
    url(r'^$', url_views.front_page, name='front_page'),
    url(r'^$', url_views.index, name='index'),
    url(r'^archive/$', url_views.archive, name='archive'),
    url(r'^(?P<year>[0-9]{4})/$', url_views.year, name='year'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', url_views.month, name='month'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', url_views.day, name='day'),
]


## This one didnt work:
# urlpatterns = [
    # url(r'^$', services.views.front_page, name='front_page'),
    # url(r'^$', services.views.index, name='index'),
    # url(r'^archive/$', services.views.archive, name='archive'),
    # url(r'^(?P<year>[0-9]{4})/$', services.views.year, name='year'),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', services.views.month, name='month'),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', services.views.day, name='day'),

## This section didnt seem to work, no module named services.views.index
## Try it in this format: 	url(r'^status/', 'core.views.status', name='status'),

# urlpatterns = [
    # url(r'^$', include('services.views.front_page', name='front_page')),
    # url(r'^$', include('services.views.index', namespace='index')),
    # url(r'^archive/$', include('services.views.archive', namespace='archive')),
    # url(r'^(?P<year>[0-9]{4})/$', include('services.views.year', namespace='year')),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', include('services.views.month', namespace='month')),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', include('services.views.day', namespace='day')),
# ]



## From woid
## This setup was giving me an error view must be callable in case of include()
## This is the format that worked in other urls.py files:
## url(r'^(?P<slug>[-_\w]+)/', include('services.urls', namespace='services')),
# urlpatterns = patterns('woid.apps.services.views',
    # url(r'^$', 'index', name='index'),
    # url(r'^archive/$', 'archive', name='archive'),
    # url(r'^(?P<year>[0-9]{4})/$', 'year', name='year'),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', 'month', name='month'),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', 'day', name='day'),
# )