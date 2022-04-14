from src.models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def as_view(request):
    tickets = Ticket.objects.all();
    return render(request, 'home.html', {'tickets': tickets})
