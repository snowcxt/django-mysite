from django.conf.urls import url
from . import views
from .api import QuestionApi

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question$', QuestionApi.as_view())
]
