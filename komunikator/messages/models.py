from django.db import models
from django.apps import apps
from api.models import User


# Create your models here.
class Message(models.Model):

    from_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='from_id')
    to_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='to_id')
    message = models.CharField(max_length=1000)
    date_time = models.DateTimeField()