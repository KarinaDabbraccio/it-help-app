from src.models import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
@login_required(login_url='/login')
def as_view(request):
    if request.method =='POST':
        currentUser = Profile.objects.get(username_id=request.user)
        newTicket = Ticket()
        newTicket.status = "O"
        newTicket.priority = request.POST["priority"]
        newTicket.description = request.POST['description']
        newTicket.title = request.POST["title"]
        if request.POST["priority"] == 'R':
            due_date = date.today() + timedelta(days=5)
        elif request.POST["priority"] == 'U':
            due_date = date.today() + timedelta(days=3)
        else:
            due_date = date.today() + timedelta(days=1)
        newTicket.due_date = due_date
        try:
            newTicket.save()
            currentUser.user_ticket.add(newTicket)
        except:
            args = {}
            text = "Submission Failed"
            args['error'] = text
            return render(request, 'createNewTicket.html', args)
        return redirect('/home')
    return render(request, 'createNewTicket.html')
