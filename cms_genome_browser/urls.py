from django.conf.urls import patterns, url
from cms_genome_browser.views import BrowserListView, BrowserDetailView, test

urlpatterns = patterns('',
    url(r'^$', BrowserListView.as_view(), name='browser_list'),
#    url(r'test', test),
    url(r'^(?P<slug>[^/]+)$', BrowserDetailView.as_view(), name='browser_detail'),
)
