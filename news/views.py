from django.views.generic import ListView, DetailView
# from django.shortcuts import redirect
from parler.views import ViewUrlMixin, TranslatableSlugMixin

from .models import Article


def _game_queryset(request, only_translations=True):
    qs = Article.objects.available(user=request.user)
    if only_translations:
        qs = qs.active_translations()
    # qs = qs.prefetch_related('translations')
    # qs = qs.prefetch_related('categories')
    # qs = qs.prefetch_related('images__file')
    # qs = Article.add_prefetch_related(qs)
    return qs


class ArticleListView(ViewUrlMixin, ListView):
    # template_name = 'news/article_list.html'
    page_template_name = 'news/article_list_page.html'
    # context_object_name = 'object_list'
    model = Article
    view_url_name = 'news:list'
    # paginate_by = 10

    # def get_queryset(self):
    #     qs = _game_queryset(self.request)
    #     return qs

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_template'] = self.page_template_name
        if 'category' in self.kwargs:
            context['category'] = self.kwargs['category']
        else:
            context['category'] = ''
        return context


class ArticleDetailView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    # model = Article
    view_url_name = 'news:detail'
    # template_name = 'articles/article_detail.html'
    # slug_field = 'code'
    # slug_url_kwarg = 'code'

    def get_queryset(self, only_translations=False):
        qs = _game_queryset(self.request, only_translations=only_translations)
        # qs = qs.prefetch_related('originalnews_set')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['random'] = self.get_queryset(only_translations=True).order_by('?')[:3]
        return context
