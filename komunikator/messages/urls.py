from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/<int:pk>', views.message_list),
    path('message/<int:pk>', views.message_detail),
    path('message/update/<int:pk>', views.message_update_delete),
    path('message/delete/<int:pk>', views.message_update_delete),
    path('friends', views.friend_list),
    path('friends/<int:pk>', views.friend_list_other),
    path('friend/<int:pk>', views.friend_detail),
    path('friend/update/<int:pk>', views.friend_update_delete),
    path('friend/delete/<int:pk>', views.friend_update_delete),
]