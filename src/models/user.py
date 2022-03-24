import uuid
from zoneinfo import ZoneInfo
from django.db import models
from django.utils.timezone import now

class User(models.Model):
    id = models.UUIDField(auto_created=True, editable=False, primary_key=True, default=uuid.uuid4)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=24)
    date_created = models.DateTimeField('Date Created', editable=False, default=now)

    @property
    def full_name(self) -> str:
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self) -> str:
        return '{full_name:s} (created: {date}, id: {id})'.format(id=self.id, full_name=self.full_name, date=(self.date_created.astimezone(ZoneInfo('America/New_York')).strftime('%x %X EST')))
