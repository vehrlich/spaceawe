from django.views.generic import TemplateView

from news.models import Article
from careers.models import Interview
from activities.models import ActivityTranslation, MetadataOption
from simplesearch.functions import get_query

from copy import copy

import logging

logger = logging.getLogger('spaceawe')


def simple_search(request):
    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title', 'teaser', 'description'])
        results = ActivityTranslation.objects.filter(entry_query)# .distinct()
        print(results)
    return


def activity_parse(query_words):
    entry_query = get_query(query_words, ['title', 'teaser', 'description'])
    results = ActivityTranslation.objects.filter(entry_query)# .distinct()
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

    def get_group_queryset(self, group_name):
        return MetadataOption.objects.filter(group__iexact=group_name).values().order_by('position')

    def get_search_filters(self, name, qs, posted_keys={}):
        """
        Returns search filter identificators for form inputs.
        Compare with posted keys if is checked or not.

        e.g. For selected level Pre-School returns [(level-pre,True), ... ]

        :param name: name of filter
        :param qs: query set with keys, values, etc for filter
        :param key: key name in qs
        :param posted_keys: name of posted filters
        :return: list of tuples (name-key, checked)
        """
        l = []
        for i in qs:
            checked = False
            visible_name = "%s: %s" % (i["group"], i["title"])
            if name in posted_keys.keys():
                if i["code"] in posted_keys.getlist(name):
                    checked = True
            l.append((name, i["code"], visible_name, checked))
        return l


    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        params = self.request.GET

        query_words = params.get('q', '')
        page = int(params.get('page', 1))
        models = params.get('models', None)


        section = 

        # get values for lists of filters and prepare filters in form's checkboxes
        age = self.get_group_queryset('age')
        filters = self.get_search_filters('age', age, params)
        time = self.get_group_queryset('time')
        filters.extend(self.get_search_filters('time', time, params))
        cost = self.get_group_queryset('cost')
        filters.extend(self.get_search_filters('cost', cost, params))
        level = self.get_group_queryset('level')
        filters.extend(self.get_search_filters('level', level, params))
        learning = self.get_group_queryset('learning')
        filters.extend(self.get_search_filters('learning', learning, params))

        if query_words:
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
        else:
            result = []
            pages_count = 0

        context['search_results'] = result
        context['pages'] = range(1, int(pages_count)+1)
        context['page'] = page
        context['query'] = query_words
        context['age'] = age
        context['time'] = time
        context['cost'] = cost
        context['level'] = level
        context['learning'] = learning
        context['filters'] = filters



        if 'category' in self.kwargs:
            context['category'] = self.kwargs['category']
        else:
            context['category'] = ''
        return context
