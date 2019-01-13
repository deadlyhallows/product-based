from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostListApiView,
    PostDetailApiView,
    PostCreateApiView,
    PostUpdateApiView,
    PostDestroyApiView

	)

urlpatterns = [
	url(r'^$', PostListApiView.as_view(), name='list'),
    url(r'^create/$', PostCreateApiView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailApiView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateApiView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDestroyApiView.as_view(), name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
