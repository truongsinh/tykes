from django.conf.urls.defaults import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('')
if settings.DEBUG:
	urlpatterns += patterns('django.views.static',
		url(r'^tykes/static/(?P<path>.*)$', 'serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True,
			}),
	)

urlpatterns += patterns('',
	# Examples:
	# url(r'^$', 'core.views.home', name='home'),
	#url(settings.LOGIN_URL, 'django.contrib.auth.views.login', name='login'),
	url(settings.LOGOUT_URL, 'django.contrib.auth.views.logout', name='logout'),
	url(r'^tykes/search/', include('haystack.urls'), name="search"),
	url(r'^tykes/admin/', include(admin.site.urls)),
	url(r'^tykes/language/', 'django.views.i18n.set_language', name="set_language"),
	url(r'^tykes/', include('entry.urls')),
	url(r'^tykes/', include('page.urls')),

)
