from django.urls import path
from src.views import home
from src.views import newTicket

urlpatterns = [
    path('', home.as_view, name='home'),
    path('', newTicket.as_view, name='newticket')
]
