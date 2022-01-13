from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person

# Create your views here.
def person_all(request):
    template = loader.get_template('person/person_all.html')
    persons = Person.objects.order_by('name')
    contex = {'persons': persons}
    return HttpResponse(template.render(contex, request))
