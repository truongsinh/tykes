from haystack import indexes
from entry.models import TopicTranslation, MethodTranslation

class TopicIndex(indexes.SearchIndex, indexes.Indexable):
	name = indexes.CharField(model_attr='name')
	text = indexes.CharField(document=True, model_attr="content")
	#pub_date = indexes.DateTimeField(model_attr='pub_date')
	def get_model(self):
		return TopicTranslation
	#def index_queryset(self):
	#	"""Used when the entire index for model is updated."""
	#	return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

class MethodIndex(indexes.SearchIndex, indexes.Indexable):
	name = indexes.CharField(model_attr='name')
	text = indexes.CharField(document=True, model_attr="content")
	#pub_date = indexes.DateTimeField(model_attr='pub_date')
	def get_model(self):
		return MethodTranslation
	#def index_queryset(self):
	#	"""Used when the entire index for model is updated."""
	#	return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())