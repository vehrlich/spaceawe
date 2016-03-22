from django.views.generic import ListView, DetailView
# from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from parler.views import ViewUrlMixin, TranslatableSlugMixin

from spaceawe import misc
from .models import Game


def _game_queryset(request, only_translations=True):
    qs = Game.objects.available(user=request.user)
    if only_translations:
        qs = qs.active_translations()
    # qs = qs.prefetch_related('translations')
    # qs = qs.prefetch_related('categories')
    # qs = qs.prefetch_related('images__file')
    # qs = Game.add_prefetch_related(qs)
    return qs


class GameListView(ViewUrlMixin, ListView):
    # template_name = 'games/game_list.html'
    page_template_name = 'games/game_list_page.html'
    # context_object_name = 'object_list'
    # model = Game
    view_url_name = 'games:list'
    # paginate_by = 10

    def get_queryset(self):
        qs = _game_queryset(self.request)
        if 'category' in self.kwargs:
            category = self.kwargs['category']
            qs = qs.filter(**{category: True})
        return qs

    def get_view_url(self):
        if 'category' in self.kwargs:
            return reverse('games:list_by_category', kwargs={'category': self.kwargs['category']})
        else:
            return super().get_view_url()

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_template'] = self.page_template_name
        return context


class GameDetailView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    # model = Game
    view_url_name = 'games:detail'
    # template_name = 'articles/article_detail.html'
    # slug_field = 'code'
    # slug_url_kwarg = 'code'

    def get_queryset(self, only_translations=False):
        qs = _game_queryset(self.request, only_translations=only_translations)
        # qs = qs.prefetch_related('originalnews_set')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['SITE_URL'] = 'http://www.spacescoop.org'  #TODO: make this configurable? inferred even?
        context['random'] = misc.spaceawe_random_resources(self.object)
        return context
