from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Message

from .seralizers import MessageSerializer


# Create your views here.

@api_view(['GET'])
def message_list(request, pk):
    user = request.user
    if request.method == 'GET':
        messages = Message.objects.filter(Q(Q(from_id=user.id) & Q(to_id=pk)) | Q(Q(from_id=pk) & Q(to_id=user.id)))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def message_update_delete(request, pk):
    user = request.user
    try:
        message = Message.objects.get(Q(from_id=user.id)&Q(pk=pk))
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = MessageSerializer(message, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
