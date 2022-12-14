from django.contrib import admin

# Register your models here.
from .models import Message, Friend


class MessageAdmin(admin.ModelAdmin):
        list_display = ['from_id', 'to_id', 'message', 'data_dodania']
        list_filter = ('from_id', 'to_id', 'data_dodania',)

admin.site.register(Message, MessageAdmin)

class FriendAdmin(admin.ModelAdmin):
        list_display = ['friend1', 'friend2']
        list_filter = ('friend1', 'friend2',)

admin.site.register(Friend, FriendAdmin)