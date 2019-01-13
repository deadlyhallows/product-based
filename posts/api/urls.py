from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostListApiView,
    # PostDetailApiView,
    # PostCreateApiView,
    # PostUpdateApiView,
    # PostDestroyApiView

	)

urlpatterns = [
	url(r'^$', PostListApiView.as_view(), name='list'),
]