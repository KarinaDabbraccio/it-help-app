from django.http import HttpResponse

def as_view(request) -> HttpResponse:
    return HttpResponse("Hello, authenticated user. You're at the login page")