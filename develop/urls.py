from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DevelopView.as_view(), name='soon_skills'),
    url(r'^support-document/(?P<pk>.+)?/$', views.SupportDocumentDetailsView.as_view(), name='support_document'),
    url(r'^assessment-tool-detail/(?P<slug>.+)?/$', views.AssessmentToolDetailView.as_view(), name='assessment_tool_detail'),
]
