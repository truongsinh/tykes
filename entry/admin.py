from django.contrib import admin
from entry.models import TopicTranslation, MethodTranslation, InstructionTranslation, Topic, Instruction, Method
from translation.admin import TranslationInline

class TopicTranslationInline(TranslationInline):
	model = TopicTranslation

class TopicAdmin(admin.ModelAdmin):
	inlines = [TopicTranslationInline]

class MethodTranslationInline(TranslationInline):
	model = MethodTranslation


class MethodAdmin(admin.ModelAdmin):
	inlines = [MethodTranslationInline]

class InstructionTranslationInline(TranslationInline):
	model = InstructionTranslation


class InstructionAdmin(admin.ModelAdmin):
	inlines = [InstructionTranslationInline]

admin.site.register(Topic, TopicAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Instruction, InstructionAdmin)
