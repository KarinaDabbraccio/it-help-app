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
                jsonReturn = json.dumps("wow");
                result = Ticket.objects.filter(ticketNum=request.POST["ticketNum"])
                jsonReturn = json.dumps(list(result.values()), indent = 4, sort_keys = True, default = str)
                return JsonResponse(jsonReturn, safe=False)
