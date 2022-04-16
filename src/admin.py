from django.contrib import admin

from src.models import Ticket
from src.models import Comment
from src.models import UserTicket

# Register your models here.
admin.site.register(Ticket)
admin.site.register(UserTicket)
admin.site.register(Comment)

