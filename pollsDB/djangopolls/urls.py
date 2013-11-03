from polls.api import PollResource, OptionResource, UserResource
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(OptionResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangopolls.views.home', name='home'),
    # url(r'^djangopolls/', include('djangopolls.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
 	url(r'^api/', include(v1_api.urls)),   
)
