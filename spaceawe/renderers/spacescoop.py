from django.core.urlresolvers import reverse
from django.utils.translation import activate
from weasyprint import HTML
from contrib.urlfetch import url_read
from urllib.parse import urljoin


def pdf(obj, path, site_url=None):
    activate(obj.language_code)  # required if called from command line
    url = urljoin(site_url, reverse('scoops:print-preview', kwargs={'code': obj.code, }))
    html_source = url_read(url)
    html_obj = HTML(string=html_source, base_url=site_url).render()
    html_obj.write_pdf(path)
