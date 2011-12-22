from django.contrib.syndication.views import Feed
from itertools import chain
from entry.models import Method, Topic

class MethodRSSFeed(Feed):
	title = "Tykes news"
	link = "/sitenews/"
	description = "Updates on changes and additions to chicagocrime.org."

	def items(self):
		#return Method.objects.order_by('-pub_date')[:5]
		result_list = list(chain(Method.objects.all()[:5],Topic.objects.all()[:5]))
		return result_list

	def item_title(self, item):
		return item.name

	def item_description(self, item):
		return item.content[:1000]