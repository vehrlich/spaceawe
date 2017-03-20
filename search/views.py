from django.views.generic import TemplateView

from news.models import Article
from careers.models import Interview, Career, Webinar
from games.models import Game
from activities.models import Activity, ActivityTranslation, MetadataOption
from spacescoops.models import Article as SpacescoopsArticle
from simplesearch.functions import get_query

# from copy import copy
from spaceawe.models import SECTIONS, CATEGORIES

import logging

logger = logging.getLogger('spaceawe')


def simple_search(request):
    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title', 'teaser', 'description'])
        results = ActivityTranslation.objects.filter(entry_query)  # .distinct()
        print(results)
    return


def activity_parse(query_words):
    entry_query = get_query(query_words, ['title', 'teaser', 'description'])
    results = ActivityTranslation.objects.filter(entry_query)  # .distinct()
    for r in results:
        r.get_absolute_url = r.master.get_absolute_url()
        r.save()
    return results


class SearchView(TemplateView):
    template_name = 'search.html'
    view_url_name = 'search:search'

    SEARCH_MODELS = {
        # name: ([models,], (available filters, ), (search_fields, )
        'news': (
            [Article, ],
            (),
            ('title', 'teaser', 'story',)
        ),
        'careers': (
            [Interview, Career, Webinar, ],
            ('category', ),
            ('title', 'teaser', 'story',)
        ),
        'games': (
            [Game, ],
            ('category', ),
            ('title', 'teaser', 'story',)
        ),
        'scoops': (
            [SpacescoopsArticle, ],
            ('category', ),
            ('title', 'story',)
        ),
        'activities': (
            [Activity, ],
            ('category', 'level', 'time', 'cost', 'kind'),
            ('title', 'teaser', 'description', 'fulldesc',)
        ),
    }

    PAGINATE_BY = 15

    def get_group_queryset(self, group_name):
        return MetadataOption.objects.filter(group__iexact=group_name).values().order_by('position')

    def get_search_harcoded_filters(self, name, data, visible_name_index, posted_keys={}, exclude_keys=[]):
        """
        Returns search filters for CATEGORIES and SECTIONS which are hardcoded
        :param name: name of group of filters
        :param data: data from which gather filters
        :param visible_name_index: on which index get data for frontend
        :param posted_keys: keys which were posted to check them
        :param exclude_keys: what to not show

        """

        l = []
        for i in data:
            checked = False
            # TODO maybe join strings in template
            visible_name = "%s: %s" % (name, data[i][visible_name_index])
            if name in posted_keys.keys():
                if i in posted_keys.getlist(name):
                    checked = True
            if name not in exclude_keys:

                l.append((i, visible_name, checked, data[i][visible_name_index]))
        return l

    def get_search_filters(self, name, qs, posted_keys={}):
        """
        Returns search filter identificators for form inputs.
        Compare with posted keys if is checked or not.

        e.g. For selected level Pre-School returns [(level-pre,True), ... ]

        :param name: name of filter
        :param qs: query set with keys, values, etc for filter
        :param key: key name in qs
        :param posted_keys: name of posted filters

        """
        l = []
        for i in qs:
            checked = False
            visible_name = "%s: %s" % (i["group"], i["title"])
            if name in posted_keys.keys():
                if str(i["id"]) in posted_keys.getlist(name):
                    checked = True
            l.append((i["id"], visible_name, checked))
        return l

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        params = self.request.GET

        query_words = params.get('q', '')
        page = int(params.get('page', 1))

        # get values for filters
        age = self.get_group_queryset('age')
        time = self.get_group_queryset('time')
        cost = self.get_group_queryset('cost')
        level = self.get_group_queryset('level')
        learning = self.get_group_queryset('learning')

        # set up filters for frontend according how models could be filtered and what is in GET
        filters = {
            'section':  self.get_search_harcoded_filters('section', SECTIONS, 'menu', params, ['skills', 'about']),
            'category': self.get_search_harcoded_filters('category', CATEGORIES, 'filter_description', params),
            'learning': self.get_search_filters('learning', learning, params),
            'level':    self.get_search_filters('level', level, params),
            'cost':     self.get_search_filters('cost', cost, params),
            'age':      self.get_search_filters('age', age, params),
            'time':     self.get_search_filters('time', time, params)
        }
        logger.info(params)
        if query_words:
            # if user wants to search in particular section:
            if params.getlist('section'):
                # filter out sections which are defined by view (not everything from GET
                sections = filter(lambda x: x in self.SEARCH_MODELS.keys(), params.getlist('section'))
            # otherwise search in all sections
            else:
                sections = self.SEARCH_MODELS.keys()

            result = []
            # different sections have different models and filters to use.
            for section in sections:
                # get which models to search in
                search_models = self.SEARCH_MODELS[section][0]
                # get available filters for search for category
                search_filters = self.SEARCH_MODELS[section][1]
                search_fields = self.SEARCH_MODELS[section][2]
                for model in search_models:
                    # get values from GET for all filters applicable for particular model
                    f = {}
                    for sf in search_filters:
                        logger.info("Get values for filter %s" % (sf))
                        # only if there is filter in GET
                        if params.getlist(sf):
                            f[sf] = params.getlist(sf)

                    logger.info("Now search in model %s with filters %s" % (model, f))
                    result.extend(
                        model.search(query_words, search_fields, f)
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



        #if 'category' in self.kwargs:
        #    context['category'] = self.kwargs['category']
        #else:
        #    context['category'] = ''
        return context
