from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DevelopView.as_view(), name='soon_skills'),
    url(r'^support-material/(?P<slug>.+)?/$', views.SupportMaterialDetailsView.as_view(), name='support_material'),
]
