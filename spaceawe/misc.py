import random

from django.db.models import Q
from django.core.urlresolvers import reverse


def spaceawe_random_resources(obj):
    return random_resources(obj.space, obj.earth, obj.navigation, obj.heritage, exclude=obj)


def random_resources(space, earth, navigation, heritage, exclude=None):
    from spacescoops.models import Article as Scoop
    from activities.models import Activity
    from games.models import Game

    tmp = []
    filtr = Q()
    if space:
        filtr = filtr | Q(space=True)
    if earth:
        filtr = filtr | Q(earth=True)
    if navigation:
        filtr = filtr | Q(navigation=True)
    if heritage:
        filtr = filtr | Q(heritage=True)

    scoops = list(Scoop.objects.filter(filtr).order_by('?')[:3])
    activities = list(Activity.objects.filter(filtr).order_by('?')[:3])
    games = list(Game.objects.filter(filtr).order_by('?')[:3])

    tmp += scoops + activities + games
    random.shuffle(tmp)

    result = []
    for item in tmp:
        if item != exclude:
            url = None
            section = None
            if type(item) is Scoop:
                url = reverse('scoops:detail', kwargs={'slug': item.slug, 'code': item.code})
                section = 'scoops'
            elif type(item) is Activity:
                url = reverse('activities:detail', kwargs={'slug': item.slug, 'code': item.code})
                section = 'activities'
            elif type(item) is Game:
                url = reverse('games:detail', kwargs={'slug': item.slug})
                section = 'games'
            result.append({'url': url, 'object': item, 'section': section, })
    return result
