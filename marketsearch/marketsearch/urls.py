"""marketsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.conf.urls import include, url

#enable the Django Admin: (recommended)
from django.contrib import admin
admin.autodiscover()

#import the function I want to call below
from services import urls as sc_urls
from core import views as urls_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	
#the following are the unique url maps for this project

#the about page from the woid app is as follows:
#	url(r'^about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
# from woid: url(r'^(?P<slug>[-_\w]+)/', include('woid.apps.services.urls', namespace='services'))
#	url(r'^(?P<slug>[-_\w]+)/', sc_urls, name='services'),
	url(r'^status/', urls_views.status, name='status'),
	
# use the about page from tinyapp
	url(r'^about/', about, name='about'),
]
