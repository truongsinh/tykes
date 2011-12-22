# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Python imports
from django.utils.translation import ugettext as _
#Django imports
from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):
	date	= models.DateTimeField(auto_now_add=True)
	context	= models.CharField(max_length="255", blank=True)
	kind	= models.NullBooleanField(blank=False,choices = (
		(True, _('Technical')),
		(False, _('Content')),
		(None, _('Other')),
		))
	contact		= models.CharField(max_length=255, blank=True)
	feedback 	= models.TextField()
	archived	= models.BooleanField(default=False)
	class Meta:
		ordering	= ['archived','-date']

