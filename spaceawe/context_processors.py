from .models import SECTIONS, CATEGORIES


def texts(request):
    return {'SECTIONS': SECTIONS, 'CATEGORIES': CATEGORIES, }
