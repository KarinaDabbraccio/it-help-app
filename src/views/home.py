from django.http import HttpResponse
from django.template import loader
from src.models import *
from django.shortcuts import render

def as_view(request):
    template = loader.get_template('home.html')
    tickets = Ticket.objects.all();
    return render(request, 'home.html', {'tickets': tickets})
