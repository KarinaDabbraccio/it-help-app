from django.db import models
from .ticket import Ticket
from .user import User

class Comment(models.Model):
    message = models.TextField()
    date_entered = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    ticketNum = models.ForeignKey(Ticket, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{ticketNum} | {message} - {author}'.format(ticketNum=self.ticketNum, message=self.message, author=self.author)