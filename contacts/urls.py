from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from contacts.models import Contact
urlpatterns = patterns('',
        url(r'^$',
            ListView.as_view(
                queryset=Contact.objects.order_by('-name'),
                context_object_name='latest_contact_list',
                template_name='contacts/index.html')),
        url(r'^(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Contact,
                template_name='contacts/detail.html')),
        )

