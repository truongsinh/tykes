from django import http
from django.conf import settings
from django.utils.translation import check_for_language

def set_language(request, lang_code):
	"""
		Base on django.views.i18n.set_language
	"""
	next = request.REQUEST.get('next', None)
	if not next:
		next = request.META.get('HTTP_REFERER', None)
	if not next:
		next = '/'
	response = http.HttpResponseRedirect(next)
	if lang_code and check_for_language(lang_code):
		if hasattr(request, 'session'):
			request.session['django_language'] = lang_code
		else:
			response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
	return response