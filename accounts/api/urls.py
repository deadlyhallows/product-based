from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateApiView,
    # UserLoginApiView

)

urlpatterns = [
    url(r'^register/$', UserCreateApiView.as_view(), name='register'),]