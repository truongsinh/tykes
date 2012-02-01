from django.conf.urls.defaults import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('')
if settings.DEBUG:
	urlpatterns += patterns('django.views.static',
		url(r'^data/(?P<path>([a-zA-Z]*/.*))$', 'serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True,
			}),
	)
	urlpatterns += patterns('django.views.static',
							url(r'^static/(?P<path>.*)$', 'serve', {
								'document_root': settings.STATIC_ROOT,
								'show_indexes': True,
								}),
							)

urlpatterns += patterns('',
	# Examples:
	# url(r'^$', 'core.views.home', name='home'),
	url(settings.LOGIN_URL, 'django.contrib.auth.views.login'),
	url(settings.LOGOUT_URL, 'django.contrib.auth.views.logout'),
	url(r'^search/', include('haystack.urls'), name="search"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^captcha/', include('captcha.urls')),
	url(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^language/', 'django.views.i18n.set_language', name="set_language"),
	url(r'', include('entry.urls')),
	url(r'^feedback/', include('feedback.urls'), name="feedback"),
	url(r'', include('page.urls')),

)
