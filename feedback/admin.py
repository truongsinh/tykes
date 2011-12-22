# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Python imports
import logging

#Django imports
from django.contrib import admin

#App imports
from models import Feedback
_ = lambda s: s

logger = logging.getLogger(__name__)

def mark_archived(modeladmin, request, queryset):
	queryset.update(archived=True)
	mark_archived.short_description = _("Mark selected feedback as archived")


class FeedbackAdmin(admin.ModelAdmin):
	list_filter = ['archived','kind']
	readonly_fields = ['date', 'context','kind', 'contact', 'feedback',]
	search_fields = ['context', 'contact', 'feedback',]
	list_display = ('contact', 'date', 'context','kind','archived')
	actions = [mark_archived]
	#def queryset(self, request):
	#	qs = super(FeedbackAdmin, self).queryset(request)
	#	if not request.GET.has_key('archived__exact'):
	#		qs = qs.filter(archived=False)
	#	return qs

admin.site.register(Feedback, FeedbackAdmin)

