from django.core.urlresolvers import reverse
from weasyprint import HTML
from contrib.urlfetch import url_read
from urllib.parse import urljoin


def pdf(obj, path, site_url=None):
    url = urljoin(site_url, reverse('scoops:print-preview', kwargs={'code': obj.code, }))
    html_source = url_read(url)
    html_obj = HTML(string=html_source, base_url=site_url).render()
    html_obj.write_pdf(path)
