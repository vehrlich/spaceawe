from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView

from develop.models import Mooc, SupportMaterial


class DevelopView(TemplateView):

    template_name = 'soon_skills.html'

    def get_context_data(self, **kwargs):
        import logging
        logger = logging.getLogger('django')

        context = super(DevelopView, self).get_context_data(**kwargs)
        context['moocs'] = Mooc.objects.all().order_by('position')
        context['support_materials'] = SupportMaterial.objects.all()

        if 'category' in self.kwargs:
            context['category'] = self.kwargs['category']
        else:
            context['category'] = ''
        logger.info(context)

        return context


class SupportMaterialDetailsView(DetailView):
    """
    Download support material
    """

    queryset = SupportMaterial.objects.all()

    def get_object(self):
        result = super().get_object()
        return result

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return redirect(obj.document_file.url)

