from django.urls import path
from src.views import home

urlpatterns = [
    path('', home.as_view, name='home')
]
