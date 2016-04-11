from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from search import views as sev
from submit import views as suv


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', sev.home),
    url(r'^submit$',suv.submit),
    url(r'^search$', sev.viewvar, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/', include('cms.urls')),
    url(r'^browser/', include('cms_genome_browser.urls', namespace='cms_genome_browser')),
    url(r'var/(?P<varid>[0-9]+)$', sev.varpage),
    url(r'gen/(?P<entrez>[0-9]+)$', sev.genpage),
    url(r'ind/(?P<indid>[0-9]+\.[0-9]+)$', sev.indpage),
    url(r'dis/(?P<omim>[0-9]+)$', sev.dispage),
    url(r'addpage$', sev.addpage),
    url(r'^ajax_list/$', sev.ajax_list, name='ajax-list'),
    url(r'^menu/$', sev.menupage),
    url(r'^menulist$', sev.menu, name='listinfo'),
)

urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
