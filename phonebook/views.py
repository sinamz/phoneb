from django.shortcuts import render_to_response
from phonebook import models as m


def home_page(request):
    contact_list = m.Contact.objects.all()
    return render_to_response('home.html', locals())


def query(request, contact_id):
    c = m.Contact.objects.get(pk=contact_id)
    return render_to_response('query.html', {'contact': c})

