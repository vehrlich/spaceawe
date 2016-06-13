from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CareersViewList.as_view(), name='list'),
    url(r'^category/(?P<category>\w+)/$', views.CareersViewList.as_view(), name='list_by_category'),
    url(r'^career/(?P<slug>.+)?/$', views.CareerDetailsView.as_view(), name='career-detail'),
    url(r'^interview/(?P<slug>.+)?/$', views.InterviewDetailsView.as_view(), name='interview-detail'),
    url(r'^webinar/(?P<slug>.+)?/$', views.WebinarDetailsView.as_view(), name='webinar-detail'),
]
