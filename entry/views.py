# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from entry.models import Topic, Method, Instruction

class TopicList(ListView):
	model = Topic
	# TODO: Language-level sorting
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(TopicList, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['topics'] = sorted(list(Topic.objects.all()),key=lambda a: a.name)
		return context

#return render_to_response('index.html')


class TopicDetail(DetailView):
	model = Topic
	context_object_name = "topic"
	# Add list for Navigation
	# TODO: Language-level sorting
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(TopicDetail, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['topics'] = sorted(list(Topic.objects.all()), key=lambda a: a.name)
		return context


class MethodList(ListView):
	model = Method
	# TODO: Language-level sorting
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(MethodList, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['methods'] = sorted(list(Method.objects.all()),key=lambda a: a.name)
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
	# TODO: Language-level sorting
	def get_context_data(self, **kwargs):
		context = super(MethodDetail, self).get_context_data(**kwargs)
		context['methods'] = sorted(list(Method.objects.all()),key=lambda a: a.name)
		return context


class InstructionExperience(DetailView):
	model = Instruction
	context_object_name = "instruction"
	# Add list for Navigation
	def get_context_data(self, **kwargs):
		context = super(InstructionExperience, self).get_context_data(**kwargs)
		return context

#return render_to_response('index.html')

