from django.http import HttpResponse
from django.template import loader

def as_view(request) -> HttpResponse:
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
