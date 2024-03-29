# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Python imports
from datetime import datetime
import logging

#Django imports
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed

#App imports
from forms import FeedbackForm

logger = logging.getLogger(__name__)

def add(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		
		if form.is_valid():
			if request.user.is_authenticated(): form.instance.user = request.user
			else: form.instance.user = None
			if 'HTTP_REFERER' in request.META:
				form.instance.context = request.META['HTTP_REFERER']
			form.save()
			return HttpResponse('', mimetype="text/plain")
		else:
			logger.debug(form.errors)
			error_msg = []
			for field in form.errors:
				for error in form.errors[field]:
					error_msg.append('%s: %s' % (form.fields[field].label, error))
			error_msg = '\n'.join(error_msg)
			
			return HttpResponseBadRequest(error_msg, mimetype="text/plain")
	else:
		return HttpResponseNotAllowed(["POST",])

