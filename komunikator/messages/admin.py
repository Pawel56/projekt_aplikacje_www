from django.contrib import admin

# Register your models here.
from .models import Message
from api.models import User

class MessageAdmin(admin.ModelAdmin):
        list_display = ['from_id', 'to_id', 'message', 'data_dodania']
        list_filter = ('from_id', 'to_id', 'data_dodania',)

admin.site.register(Message, MessageAdmin)