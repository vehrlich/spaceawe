from django.core.urlresolvers import reverse
from django.utils.translation import activate
from weasyprint import HTML
from contrib.urlfetch import url_read
from urllib.parse import urljoin


def pdf(obj, path, site_url=None):
    activate(obj.language_code)  # required if called from command line

    # first page
    header_url = urljoin(site_url, reverse('activities:print-preview-header', kwargs={'code': obj.code, }))
    header_html_source = url_read(header_url)
    header = HTML(string=header_html_source, base_url=site_url).render()

    # other pages
    content_url = urljoin(site_url, reverse('activities:print-preview-content', kwargs={'code': obj.code, }))
    content_html_source = url_read(content_url)
    content = HTML(string=content_html_source, base_url=site_url).render()

    header.pages += content.pages

    header.write_pdf(path)
