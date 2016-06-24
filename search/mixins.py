from django.db.models import Q

class SearchModel(object):

    search_fields = ('title', 'teaser', 'story',)

    @classmethod
    def get_query(cls, query_string):
        query = Q()
        for field in cls.search_fields:
            query |= Q(**{'translations__%s__icontains' % field: query_string})
        return query

    @classmethod
    def search(cls, query_string):
        if not query_string:
            return []
        query = cls.get_query(query_string)
        objects = list(cls.objects.filter(query))
        return objects
