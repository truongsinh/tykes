from django.conf.urls.defaults import patterns, url
from entry.views import TopicList, MethodList, MethodDetail, TopicDetail, InstructionExperience
from entry.feed import MethodRSSFeed

urlpatterns = patterns('',
	url(r'^rss', MethodRSSFeed(), name="rss"),
	url(r'^methods', MethodList.as_view(), name="methods"),
	url(r'^topics', TopicList.as_view(), name="topics"),
	url(r'^method/(?P<pk>\d+)', MethodDetail.as_view(), name="method"),
	url(r'^topic/(?P<pk>\d+)', TopicDetail.as_view(), name="topic"),
	url(r'^experience/(?P<pk>\d+)', InstructionExperience.as_view(), name="experience"),


)
