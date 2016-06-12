from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, View, TemplateView
from django.core.urlresolvers import reverse
from parler.views import ViewUrlMixin, TranslatableSlugMixin

from spaceawe import misc
from .models import Interview, Career, Webinar

class CareersViewList(ViewUrlMixin, TemplateView):
    template_name = 'careers.html'
    view_url_name = 'careers:list'

    def filter_category(self, queryset):
        if 'category' in self.kwargs:
            category = self.kwargs['category']
            queryset = queryset.filter(**{category: True})
        return queryset

    def get_careers_queryset(self):
        queryset = Career.objects.all()
        queryset = self.filter_category(queryset)
        return queryset

    def get_interviews_queryset(self):
        queryset = Interview.objects.all()
        queryset = self.filter_category(queryset)
        return queryset

    def get_webinars_queryset(self):
        queryset = Webinar.objects.all()
        queryset = self.filter_category(queryset)
        return queryset

    def get_view_url(self):
        if 'category' in self.kwargs:
            return reverse('careers:list_by_category', kwargs={'category': self.kwargs['category']})
        else:
            return super().get_view_url()

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.template_name]
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_template'] = self.template_name
        context['interviews'] = self.get_interviews_queryset()
        context['careers'] = self.get_careers_queryset()
        context['webinars'] = self.get_webinars_queryset()
        return context


class CareerDetailsView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    view_url_name = 'careers:career-detail'
    template_name = 'careers/detail.html'

    def get_queryset(self):
        queryset = Career.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InterviewDetailsView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    view_url_name = 'careers:interview-detail'
    template_name = 'interviews/detail.html'

    def get_queryset(self):
        queryset = Interview.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WebinarDetailsView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    view_url_name = 'careers:webinar-detail'
    template_name = 'webinars/detail.html'

    def get_queryset(self):
        queryset = Webinar.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
