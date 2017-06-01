from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/', permanent=False), name='contests'),
    url(r'^(?P<slug>.+)?/$', views.ContestView.as_view(), name='contest-detail'),

]
