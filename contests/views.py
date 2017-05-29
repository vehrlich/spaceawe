from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.views.generic import DetailView
from parler.views import ViewUrlMixin, TranslatableSlugMixin
from .models import Contest

class ContestView(TranslatableSlugMixin, DetailView):
    model = Contest
    template_name = 'contest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
