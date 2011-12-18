from django.contrib.syndication.views import Feed
from entry.models import Method

class MethodRSSFeed(Feed):
	title = "Tykes news"
	link = "/sitenews/"
	description = "Updates on changes and additions to chicagocrime.org."

	def items(self):
		#return Method.objects.order_by('-pub_date')[:5]
		return Method.objects.all()[:5]

	def item_title(self, item):
		return item.name

	def item_description(self, item):
		return item.content