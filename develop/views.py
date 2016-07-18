from django.views.generic import TemplateView

from develop.models import Mooc

class DevelopView(TemplateView):

    template_name = 'spaceawe/soon_skills.html'

    def get_context_data(self, **kwargs):
        context = super(DevelopView, self).get_context_data(**kwargs)
        context['moocs'] = Mooc.objects.all().order_by('position')
        return context
