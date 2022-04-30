from src.models import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from src.models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder



@login_required(login_url='/login')
def as_view(request):
        if request.method == 'POST':
                #check to see who is logged in
                currentUser = Profile.objects.get(username_id=request.user)
                currentUserGroup = getattr(currentUser, 'user_group')

                if ('alltickets' in request.POST) and (currentUserGroup=='T'):
                    status = ""
                    priority = ""
                    assigned = "A"
                    postInfo = ""
                elif ('mytickets' in request.POST) or (('alltickets' in request.POST) and (currentUserGroup=='U')):
                    result = Profile.objects.get(username=request.user)
                    jsonReturn = json.dumps(list(result.user_ticket.all().values()), indent = 4, sort_keys = True, default = str)
                    return JsonResponse(jsonReturn, safe=False)
                else:
                    postInfo = request.POST['post_id']
                    status = request.POST['status']
                    priority = request.POST['priority']
                    assigned = request.POST['assigned']
                if status == "A":
                    status = ""
                if priority == "A":
                    priority = ""
                if assigned == "NA":
                    assigned = False
                elif assigned == "AS":
                    assigned = True
                if postInfo.isdigit():
                    if assigned =="A":
                        result = Ticket.objects.filter(ticketNum__icontains=postInfo, status__contains=status, priority__contains=priority)
                    else:
                        result = Ticket.objects.filter(ticketNum__icontains=postInfo, status__contains=status, priority__contains=priority,is_assigned=assigned)
                else:
                    if assigned =="A":
                        result = Ticket.objects.filter(title__icontains=postInfo, status__contains=status, priority__contains=priority)
                    else:
                        result = Ticket.objects.filter(title__icontains=postInfo, status__contains=status, priority__contains=priority,is_assigned=assigned)
                result = result.order_by('ticketNum')
                jsonReturn = json.dumps(list(result.values()), indent = 4, sort_keys = True, default = str)
                return JsonResponse(jsonReturn, safe=False)
