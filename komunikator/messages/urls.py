from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/<int:pk>', views.message_list),
    path('message/update/<int:pk>', views.message_update_delete),
    path('message/delete/<int:pk>', views.message_update_delete),
]