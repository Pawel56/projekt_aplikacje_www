from django.db import models
from django.apps import apps
from api.models import User


# Create your models here.
class Message(models.Model):

    from_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='from_id', blank=True,
                                null=True)
    to_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='to_id', blank=True,
                              null=True)
    message = models.CharField(max_length=1000)
    data_dodania = models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
    friend1 = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='friend1', blank=True,
                                null=True)
    friend2 = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='friend2', blank=True,
                                null=True)
