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
    ticketNum = models.IntegerField(primary_key=True)
    is_assigned = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, default='O')
    priority = models.CharField(max_length=1, choices=PRIOIRTY_TYPE)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateTimeField(null=True)
    date_closed = models.DateTimeField(null=True)


class User(models.Model):
    USER_TYPE = [
        ('C', 'Customer'),
        ('T', 'Tech')
    ]
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_group = models.CharField(max_length=1, choices=USER_TYPE)
    ticket = models.ManyToManyField(Ticket)


class Comment(models.Model):
    message = models.TextField()
    date_entered = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)