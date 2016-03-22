from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='list'),
    url(r'^category/(?P<category>\w+)/$', views.GameListView.as_view(), name='list_by_category'),

    url(r'^(?P<slug>.+)?/$', views.GameDetailView.as_view(), name='detail'),
]
