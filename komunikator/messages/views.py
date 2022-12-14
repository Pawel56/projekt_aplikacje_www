from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Message, Friend

from .seralizers import MessageSerializer, FriendSerializer, MessageCreateSerializer, FriendCreateSerializer


# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def message_list(request, pk):
    user = request.user
    if request.method == 'GET':
        messages = Message.objects.filter(Q(Q(from_id=user.id) & Q(to_id=pk)) | Q(Q(from_id=pk) & Q(to_id=user.id)))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def message_detail(request, pk):
    user = request.user
    try:
        message = Message.objects.get(Q(pk=pk) & Q(Q(from_id=user.id) | Q(to_id=user.id)))
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def message_update_delete(request, pk):
    user = request.user
    try:
        message = Message.objects.get(Q(from_id=user.id) & Q(pk=pk))
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MessageSerializer(message, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def message_create(request):
    user = request.user
    message = Message(from_id=user)

    if request.method == "POST":

        serializer = MessageCreateSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def friend_detail(request, pk):
    try:
        friend = Friend.objects.filter(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FriendSerializer(friend, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def friend_list(request):
    user = request.user
    if request.method == 'GET':
        friends = Friend.objects.filter(Q(friend1=user.id) | Q(friend2=user.id))
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def friend_list_other(request, pk):
    if request.method == 'GET':
        friends = Friend.objects.filter(Q(friend1=pk) | Q(friend2=pk))
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def friend_update_delete(request, pk):
    try:
        friend = Friend.objects.filter(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if friend.friend1 != user or friend.friend2 != user:
        return Response({'response': "You don't have permission to edit that"})

    if request.method == 'GET':
        serializer = FriendSerializer(friend, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FriendSerializer(friend, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        friend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def friend_create(request):
    user = request.user
    friend = Friend(friend1=user)

    if request.method == "POST":

        serializer = FriendCreateSerializer(friend, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)