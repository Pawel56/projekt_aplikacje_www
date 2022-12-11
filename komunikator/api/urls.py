from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  path('auth/', include('rest_auth.urls')),
  path('users', views.user_list),
  path('users/search/<str:name>', views.user_search),
]