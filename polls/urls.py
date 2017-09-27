from django.conf.urls import url
from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question$', api.QuestionApi.as_view()),
]
