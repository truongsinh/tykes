from django.contrib import admin
from entry.models import TopicTranslation, MethodTranslation, InstructionTranslation, Topic, Instruction, Method
from multilingual_model.admin import TranslationInline
from settings import MEDIA_URL

class TopicTranslationInline(TranslationInline):
	model = TopicTranslation


class TopicAdmin(admin.ModelAdmin):
	inlines = [TopicTranslationInline]

	class Media:
		js = (	"%s%s" % (MEDIA_URL, 'theme/jquery.min.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/conf.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/jquery.tinymce.js'),)

#list_filter = ('topictranslation__language',)


class MethodTranslationInline(TranslationInline):
	model = MethodTranslation


class MethodAdmin(admin.ModelAdmin):
	inlines = [MethodTranslationInline]

	class Media:
		js = (	"%s%s" % (MEDIA_URL, 'theme/jquery.min.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/conf.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/jquery.tinymce.js'),)

#list_filter = ('methodtranslation__language',)


class InstructionTranslationInline(TranslationInline):
	model = InstructionTranslation


class InstructionAdmin(admin.ModelAdmin):
	inlines = [InstructionTranslationInline]

	class Media:
		js = (	"%s%s" % (MEDIA_URL, 'theme/jquery.min.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/conf.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/jquery.tinymce.js'),)

#list_filter = ('instructiontranslation__language',)

admin.site.register(Topic, TopicAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Instruction, InstructionAdmin)
