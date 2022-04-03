from django.contrib import admin

from src.models import User
from src.models import Ticket
from src.models import Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Comment)

