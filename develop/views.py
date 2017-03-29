from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView
from django.db.models import Count
from parler.views import ViewUrlMixin, TranslatableSlugMixin

from develop.models import Mooc, AssessmentTool, AssessmentMetadataOption, SupportDocument

import logging
logger = logging.getLogger('spaceawe')


class DevelopView(TemplateView):

    template_name = 'soon_skills.html'

    def get_assessment_tools(self):
        # , atype):
        """
        :return:Returns Assessment tools grouped by assessment type
        """
        return AssessmentTool.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DevelopView, self).get_context_data(**kwargs)
        context['moocs'] = Mooc.objects.all().order_by('position')
        context['assessment_tools'] = self.get_assessment_tools()

        if 'category' in self.kwargs:
            context['category'] = self.kwargs['category']
        else:
            context['category'] = ''

        return context


class SupportDocumentDetailsView(DetailView):
    """
    Download support material
    """

    queryset = SupportDocument.objects.all()
    # TODO dowload in active language
    def get_object(self):
        result = super().get_object()
        return result

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return redirect(obj.document_file.url)


class AssessmentToolDetailView(ViewUrlMixin, TranslatableSlugMixin, DetailView):
    view_url_name = 'develop:assessment_tool_detail'
    template_name = 'assessment_tool_detail.html'

    def get_queryset(self):
        queryset = AssessmentTool.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AssessmentToolDetailView, self).get_context_data(**kwargs)
        return context

