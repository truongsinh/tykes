# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from entry.models import Topic, Method, Instruction

class TopicList(ListView):
	model = Topic
	queryset = Topic.objects.all()
	#queryset = Topic.objects.filter(translations__language_code=get_language())
	context_object_name = "topics"

#return render_to_response('index.html')


class TopicDetail(DetailView):
	model = Topic
	context_object_name = "topic"
	# Add list for Navigation
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(TopicDetail, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['topics'] = Topic.objects.all()
		return context


class MethodList(ListView):
	model = Method
	context_object_name = "methods"

	def get_context_data(self, **kwargs):
		context = super(MethodList, self).get_context_data(**kwargs)
		'''
		context['paths']=[
			[reverse("home"), _("Home")],
			[reverse("methods"), _("Methods")],
		]
		'''
		return context


class MethodDetail(DetailView):
	model = Method
	context_object_name = "method"
	# Add list for Navigation
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(MethodDetail, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['methods'] = Method.objects.all()

	def get_context_data(self, **kwargs):
		context = super(MethodDetail, self).get_context_data(**kwargs)
		return context


class InstructionExperience(DetailView):
	model = Instruction
	context_object_name = "instruction"
	# Add list for Navigation
	def get_context_data(self, **kwargs):
		context = super(InstructionExperience, self).get_context_data(**kwargs)
		return context

#return render_to_response('index.html')

