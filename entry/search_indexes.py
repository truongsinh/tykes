from haystack import indexes
from entry.models import TopicTranslation, MethodTranslation

class TopicIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
	name = indexes.CharField(model_attr='name')
	text = indexes.CharField(document=True, model_attr="content")
	#pub_date = indexes.DateTimeField(model_attr='pub_date')
	def get_model(self):
		return TopicTranslation

class MethodIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
	name = indexes.CharField(model_attr='name')
	text = indexes.CharField(document=True, model_attr="content")
	#pub_date = indexes.DateTimeField(model_attr='pub_date')
	def get_model(self):
		return MethodTranslation