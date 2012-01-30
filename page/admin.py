from django.contrib import admin
from page.models import PageTranslation, Page

class PageTranslationInline(admin.StackedInline):
	model = PageTranslation


class PageAdmin(admin.ModelAdmin):
	inlines = [PageTranslationInline]

admin.site.register(Page, PageAdmin)
