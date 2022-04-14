from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from src.models.ticket import Ticket

def as_view(request) -> HttpResponse:
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# Function to show the Ticket objects on the home template
def showtickets(request):
    tickets = Ticket.objects
    return render(request, 'home.html', { 'tickets':tickets } )
    
