from django.conf.urls import patterns, include, url
from polls.api import PollResource, ChoiceResource
from django.contrib import admin
admin.autodiscover()

poll_resource = PollResource()
# Choice_resource = ChoiceResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangopolls.views.home', name='home'),
    # url(r'^djangopolls/', include('djangopolls.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
 	url(r'^api/', include(poll_resource.urls)),   
)
