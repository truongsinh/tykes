# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Django imports
from django import forms
from django.forms.widgets import Select
from django.utils.translation import ugettext as _

#App imports
from captcha.fields import CaptchaField
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
	captcha = CaptchaField()

	class Meta:
		model = Feedback
		fields = ('kind', 'contact', 'feedback',)
