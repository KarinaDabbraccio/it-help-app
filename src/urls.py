from django.urls import path
from src.views import home, searchticket, newTicket

urlpatterns = [
    path('', home.as_view, name='home'),
    path('', newTicket.as_view, name='newticket'),
    path('', searchticket.as_view, name='searchticket')
]
