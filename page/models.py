from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from translation.models import MultilingualModel, MultilingualTranslation
# Create your models here.
class PageTranslation(MultilingualTranslation):
	parent = models.ForeignKey("Page", related_name="translations")
	name = models.CharField(max_length=255)
	content = RichTextField(blank=True)
	def __unicode__(self):
		return u"%s - %s: %s" % (self.parent, self.language_code, self.name)

	class Meta:
		ordering = ['name']


class Page(MultilingualModel):
	slug = models.SlugField(primary_key=True)

	def __unicode__(self):
		return u"[%s] %s" % (self.unicode_wrapper("slug"), self.unicode_wrapper("name"))

	def get_absolute_url(self):
		return reverse('page', args=[self.slug])

	url = property(get_absolute_url)

	def get_admin_url(self):
		return reverse('admin:page_page_change', args=(self.slug,))

	admin_url = property(get_admin_url)