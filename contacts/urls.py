from django.conf.urls import patterns, include, url

urlpatterns = patterns('contacts.views',
        url(r'^$', 'index'),
        url(r'^$(?P<contact_id>\d+)/$', 'detail'),
        )


