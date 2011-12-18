from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from page.views import Page, PlaceHolder

admin.autodiscover()

urlpatterns = patterns('',
	url(r'(?P<slug>[a-zA-Z0-9_.-]+)', Page.as_view(), name="page"),
	url(r'', Page.as_view(), {'slug': "home"}, name="home"),


)
