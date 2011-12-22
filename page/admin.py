from django.contrib import admin
from page.models import PageTranslation, Page, Attachment
from translation.admin import TranslationInline
from settings import MEDIA_URL

class AttachmentInline(admin.TabularInline):
	model = Attachment

class PageTranslationInline(admin.StackedInline):
	model = PageTranslation
	inlines = [
		AttachmentInline,
		]
class PageTranslationAdmin(admin.ModelAdmin):
	inlines = [
		AttachmentInline,
		]
	class Media:
		js = (	"%s%s" % (MEDIA_URL, 'theme/jquery.min.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/conf.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/jquery.tinymce.js'),)


class PageAdmin(admin.ModelAdmin):
	inlines = [PageTranslationInline]

	class Media:
		js = (	"%s%s" % (MEDIA_URL, 'theme/jquery.min.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/conf.js'),
				  "%s%s" % (MEDIA_URL, 'tiny_mce/jquery.tinymce.js'),)

#list_filter = ('topictranslation__language',)

admin.site.register(Page, PageAdmin)
admin.site.register(PageTranslation, PageTranslationAdmin)
