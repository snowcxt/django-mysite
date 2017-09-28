from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^load-auth$', api.load_auth_view),
    url(r'^login$', api.login_view),
    url(r'^logout$', api.logout_view),
]
