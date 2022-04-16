import uuid
from zoneinfo import ZoneInfo
from django.db import models
from django.utils.timezone import now
from .ticket import Ticket
from django.contrib.auth.models import User

class UserTicket(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_ticket = models.ManyToManyField(Ticket, blank=True)

    def __str__(self) -> str:
        return 'User: {user_id}'.format(user_id=self.user_id)
