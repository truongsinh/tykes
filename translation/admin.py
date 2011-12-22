from django.contrib import admin

from translation.forms import TranslationFormSet
from translation import settings

MAX_LANGUAGES = len(settings.LANGUAGES)


class TranslationInline(admin.StackedInline):
	def __init__(self, *args, **kwargs):
		super(TranslationInline, self).__init__(*args, **kwargs)
		if settings.AUTO_HIDE_LANGUAGE:
			self.exclude = ('language_code', )
			self.can_delete = False

	extra = 1
	formset = TranslationFormSet
	max_num = MAX_LANGUAGES
