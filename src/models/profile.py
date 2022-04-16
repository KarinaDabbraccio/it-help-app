from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .ticket import Ticket

class Profile(models.Model):

    USER_TYPE = [
        ('C', 'Customer'),
        ('T', 'Tech')
    ]

    '''
    Extends Django's default user.model    
    Fields that are included:

    first_name: blank=true, 150 char
    last_name: blank=true, 150 char
    email: blank=true, email
    password: hashed password

    groups: many-to-many relations - ignore this
    user_permissions: many-to-many relations - ignore this
    is_staff: boolean to admin site access - set to false
    is_active: boolean to flag account - set to true
    is_supersuer: boolean for all access - set to false

    last_login: datetime, auto generated last login
    date_joined: datetime, auto generated when created
    '''
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    '''
    Custom fields for user.profile model in this app. 
    '''
    user_group = models.CharField(max_length=1, choices=USER_TYPE)
    user_ticket = models.ManyToManyField(Ticket, blank=True)

    '''
    This updates default user model with our profile extention
    '''
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()