import uuid
from zoneinfo import ZoneInfo
from django.db import models
from django.utils.timezone import now
from .ticket import Ticket

class User(models.Model):

    USER_TYPE = [
        ('C', 'Customer'),
        ('T', 'Tech')
    ]

    id = models.UUIDField(auto_created=True, editable=False, primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=24)
    date_created = models.DateTimeField('Date Created', editable=False, default=now)
    user_group = models.CharField(max_length=1, choices=USER_TYPE)
    ticketNum = models.ManyToManyField(Ticket, blank=True)

    @property
    def full_name(self) -> str:
        return '%s %s' % (self.first_name, self.last_name)
    
    def __str__(self) -> str:
        return '{full_name:s} ({user_group})'.format(full_name=self.full_name, user_group=self.user_group)
