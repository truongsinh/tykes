# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from page.models import Page


class PlaceHolder(TemplateView):
	model = Page
	context_object_name = "page"
	template_name = "layout.html"


class Page(DetailView):
	model = Page
	context_object_name = "page"
	#template_name = "page.html"