from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^load-auth$', api.load_auth),
]
