from django.views.generic import TemplateView

from news.models import Article
from careers.models import Interview
from activities.models import ActivityTranslation
from simplesearch.functions import get_query

from copy import copy

def simple_search(request):
    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title', 'teaser','description'])
        results = ActivityTranslation.objects.filter(entry_query).distinct()
        print(results)
    return

def activity_parse(query_words):
    entry_query = get_query(query_words, ['title', 'teaser','description'])
    results = ActivityTranslation.objects.filter(entry_query).distinct()
    for r in results:
         r.get_absolute_url = r.master.get_absolute_url()
         r.save()
    return results

class SearchView(TemplateView):
    template_name = 'search.html'
    view_url_name = 'search:search'

    SEARCH_MODELS = [
        Article,
        Interview,
    ]

    PAGINATE_BY = 15

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        request = self.request
        params = request.GET
        query_words = params.get('q', '')
        page = int(params.get('page', 1))
        models = params.get('models', None)

        search_models = copy(self.SEARCH_MODELS)
        if models is not None:
            search_models = filter(lambda x: x.__class__.__name__ in models, search_models)
        result = []
        for model in search_models:
            result.extend(
                model.search(query_words)
            )
        activity_results = activity_parse(query_words)
        result = list(result)
        result.extend(activity_results)
        pages_count = (len(result) / self.PAGINATE_BY) + 1
        result = result[(page-1)*self.PAGINATE_BY:page*self.PAGINATE_BY]

        context['search_results'] = result
        context['pages'] = range(1, int(pages_count)+1)
        context['page'] = page
        if 'category' in self.kwargs:
            context['category'] = self.kwargs['category']
        else:
            context['category'] = ''
        return context
