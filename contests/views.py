from django.views.generic import DetailView
from django.http import Http404
from parler.views import ViewUrlMixin, TranslatableSlugMixin
from .models import Contest


class ContestView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    view_url_name = 'contests:contest-detail'
    model = Contest
    template_name = 'contest.html'

    def get_queryset(self):
        qs = Contest.objects.available(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LatestCompetitionView(DetailView):
    model = Contest
    template_name = 'contest.html'

    def get_object(self, queryset=None):
        try:
            qs = Contest.objects.available(user=self.request.user).latest('release_date')
        except:
            raise Http404
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context