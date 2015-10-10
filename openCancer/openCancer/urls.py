from django.conf.urls import patterns, include, url
from patient import views
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openCancer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^patient/', include('patient.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
