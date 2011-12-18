from django.core.urlresolvers import reverse
from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from SearchEngine import SearchManager

class TopicTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Topic", related_name="translations")
	name = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now=True)
	content = models.TextField(blank=True)
	theses = models.TextField(blank=True)			#	List of links to theseus
	papers = models.TextField(blank=True)			#	List of links to papers from different sources

	def __unicode__(self):
		return u"%s - %s: %s" % (self.parent, self.language_code, self.name)

	class Meta:
		ordering = ['last_updated']

class Topic(MultilingualModel):
	def __unicode__(self):
		return self.unicode_wrapper("name")

	def get_absolute_url(self):
		return reverse('topic', args=[self.id])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:core_topic_change', args=(self.id,))

	admin_url = property(get_admin_url)

	def get_link(self):
		return '<a href="%s">%s</a>' % (self.url, self.name)

	link = property(get_link)


class MethodTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Method", related_name="translations")
	name = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now=True)
	content = models.TextField(blank=True)	#	Short desc
	full = models.FileField(upload_to="methods", blank=True)		   #   Full method /PDF
	theses = models.TextField(blank=True)			#	List of links to theseus
	papers = models.TextField(blank=True)			#	List of links to papers from different sources

	def __unicode__(self):
		return u"%s - %s: %s" % (self.parent, self.language_code, self.name)

	class Meta:
		ordering = ['last_updated']


class Method(MultilingualModel):
	topics = models.ManyToManyField(Topic, through="Instruction", related_name="methods")

	def __unicode__(self):
		return self.unicode_wrapper("name")

	def get_absolute_url(self):
		return reverse('method', args=[self.id])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:core_method_change', args=(self.id,))

	admin_url = property(get_admin_url)

	def get_link(self):
		return '<a href="%s">%s</a>' % (self.url, self.name)

	link = property(get_link)


class InstructionTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Instruction", related_name="translations")
	last_updated = models.DateTimeField(auto_now=True)
	instruction = models.FileField(upload_to="instructions",
		blank=True)	#   Instruction of how to use method to particular topics /PDF
	experience = models.TextField(blank=True)	 #   Experience /HTML
	theses = models.TextField(blank=True)			#	List of links to theseus
	papers = models.TextField(blank=True)			#	List of links to papers from different sources
	content = property(experience)
	def __unicode__(self):
		return u"[%s] %s" % (self.language_code, self.parent)


class Instruction(MultilingualModel):
	method = models.ForeignKey(Method, related_name="instructions")
	topic = models.ForeignKey(Topic, related_name="instructions")

	class Meta:
		unique_together = ("method", "topic")

	def __unicode__(self):
		return u"%s - %s" % (self.method, self.topic)

	def get_absolute_url(self):
		return reverse('experience', args=[self.id])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:core_instruction_change', args=(self.id,))

	admin_url = property(get_admin_url)