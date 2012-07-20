# Create your views here.
from contacts.models import Contact, ContactForm
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    c = Contact.objects.all()
    return render_to_response('contacts/index.html', {'contact_list':
        c})

def detail(request, contact_id):
    c = Contact.objects.get(pk=contact_id)
    return render_to_response('contacts/detail.html', {'contact': c})

def addcontact(request):
    if request.method == 'POST'
        form = ContactForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()

        return render_to_response('contact.html', {'form': form, })
