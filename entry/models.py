from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from translation.models import MultilingualModel, MultilingualTranslation

class TopicTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Topic", related_name="translations")
	name = models.CharField(max_length=255)
	content = RichTextField(blank=True)
	theses = RichTextField(blank=True)			#	List of links to theseus
	papers = RichTextField(blank=True)			#	List of links to papers from different sources

	def __unicode__(self):
		return u"%s - %s: %s" % (self.parent, self.language_code, self.name)


class Topic(MultilingualModel):
	last_updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.unicode_wrapper("name")

	def get_absolute_url(self):
		return reverse('topic', args=[self.id])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:entry_topic_change', args=(self.id,))

	admin_url = property(get_admin_url)

	def get_link(self):
		return '<a href="%s">%s</a>' % (self.url, self.name)

	link = property(get_link)
	class Meta:
		ordering = ['-last_updated']


class MethodTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Method", related_name="translations")
	name = models.CharField(max_length=255)
	content = RichTextField(blank=True)	#	Short desc
	full = models.FileField(upload_to="method", blank=True)		   #   Full method /PDF
	theses = RichTextField(blank=True)			#	List of links to theseus
	papers = RichTextField(blank=True)			#	List of links to papers from different sources

	def __unicode__(self):
		return u"%s - %s: %s" % (self.parent, self.language_code, self.name)

class Method(MultilingualModel):
	topics = models.ManyToManyField(Topic, through="Instruction", related_name="methods")

	last_updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-last_updated']

	def __unicode__(self):
		return self.unicode_wrapper("name")

	def get_absolute_url(self):
		return reverse('method', args=[self.id])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:entry_method_change', args=(self.id,))

	admin_url = property(get_admin_url)

	def get_link(self):
		return '<a href="%s">%s</a>' % (self.url, self.name)

	link = property(get_link)


class InstructionTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Instruction", related_name="translations")
	instruction = models.FileField(upload_to="instruction",
		blank=True)	#   Instruction of how to use method to particular topics /PDF
	experience = RichTextField(blank=True)	 #   Experience /HTML
	theses = RichTextField(blank=True)			#	List of links to theseus
	papers = RichTextField(blank=True)			#	List of links to papers from different sources
	content = property(experience)
	def __unicode__(self):
		return u"[%s] %s" % (self.language_code, self.parent)

class Instruction(MultilingualModel):
	method = models.ForeignKey(Method, related_name="instructions")
	topic = models.ForeignKey(Topic, related_name="instructions")
	last_updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-last_updated']
		unique_together = ("method", "topic")

	def __unicode__(self):
		return u"%s - %s" % (self.method, self.topic)

	def get_absolute_url(self):
		return reverse('experience', args=[self.id])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:entry_instruction_change', args=(self.id,))

	admin_url = property(get_admin_url)