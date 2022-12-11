from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import User
from .serializers import UserSerializer, UserSearchSerializer

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_search(request, name):
    if request.method == 'GET':
        if name.__contains__(" "):
            user_names = name.split(" ")
            users = User.objects.filter(Q(first_name__contains=user_names[0]) & Q(last_name__contains=user_names[1]))
        else:
            users = User.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name))
        serializer = UserSearchSerializer(users, many=True)
        return Response(serializer.data)

