from src.models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.shortcuts import render

@cache_control(no_cache=True, must_revalidate=True)
def as_view(request):
    logout(request)
    render (request, 'login.html')