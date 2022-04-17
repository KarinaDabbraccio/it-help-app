from src.models import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from src.models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from itertools import chain


'''
ticketResult get all the values for the ticket clicked
commetResults gets the values for username, user_group, message and date entered
result joins the 2 querysets together
'''
@login_required(login_url='/login')
def as_view(request):
        if request.method == 'POST':
                jsonReturn = json.dumps("wow");
                ticketResult = Ticket.objects.filter(ticketNum=request.POST["ticketNum"])
                commentResult = Comment.objects.filter(ticketNum=request.POST["ticketNum"])
                result = chain(ticketResult.values(), commentResult.values('message', 'user__username', 'user__profile__user_group', 'date_entered'))
                jsonReturn = json.dumps(list(result), indent = 4, sort_keys = True, default = str)
                return JsonResponse(jsonReturn, safe=False)
