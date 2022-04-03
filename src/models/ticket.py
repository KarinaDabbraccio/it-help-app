from django.db import models


class Ticket(models.Model):
    STATUS_TYPE = [
        ('O', 'Open'),
        ('C', 'Closed')
    ]
    PRIOIRTY_TYPE = [
        ('R', 'Routine'),
        ('U', 'Urgent'),
        ('E', 'Emergency')
    ]
    ticketNum = models.AutoField(auto_created=True, primary_key=True)
    is_assigned = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, default='O')
    priority = models.CharField(max_length=1, choices=PRIOIRTY_TYPE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateTimeField(null=True, blank=True)
    date_closed = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return 'Ticket: {ticketNum} - {title}'.format(ticketNum=self.ticketNum, title=self.title)