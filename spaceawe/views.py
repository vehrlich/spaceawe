# from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView
from django.http import Http404

from parler.views import ViewUrlMixin
from parler.utils.context import switch_language
from el_pagination.decorators import page_template

from django_ext.models.spaceawe import CATEGORIES
from spacescoops.models import Article
from activities.models import Activity
from games.models import Game

from news.models import Highlight
from institutions.models import Person


def home(request):
    return render(request, 'spaceawe/home.html', {
        'highlights': Highlight.objects.all(),
    })


def about(request):
    q = Q(spaceawe_partner=True) | Q(spaceawe_node=True)
    q = q & Q(institution__location__latitude__isnull=False)
    q = q & Q(institution__location__longitude__isnull=False)
    return render(request, 'spaceawe/about.html', {
        'partners': Person.objects.filter(q).select_related('institution').order_by('spaceawe_partner'),
    })


@page_template('spacescoops/article_list_page_in_category.html', key='scoops_page')
@page_template('games/game_list_page_in_category.html', key='games_page')
@page_template('activities/activity_list_page_in_category.html', key='activities_page')
def categories(request, code, template='spaceawe/categories.html', extra_context=None):
    if code not in CATEGORIES.keys():
        raise Http404
    context = {
        'scoops': Article.add_prefetch_related(Article.objects.filter(**{code: True}).active_translations())[:3],
        'games': Game.objects.available().filter(**{code: True})[:3],
        'activities': Activity.objects.available().filter(**{code: True})[:3],
        'spaceawe_category': code,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


class TranslatableTemplateView(ViewUrlMixin, TemplateView):
    pass
