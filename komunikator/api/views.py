from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer, UserSearchSerializer

@api_view(['GET'])
@permission_required('api.view_user')
@permission_classes((IsAuthenticated,))
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_required('api.view_user')
@permission_classes((IsAuthenticated,))
def user_detail(request, pk):
    user = request.user
    try:
        friend = User.objects.filter(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(friend)
        return Response(serializer.data)

@api_view(['GET'])
@permission_required('api.view_user')
@permission_classes((IsAuthenticated,))
def user_search(request, name):
    if request.method == 'GET':
        if name.__contains__(" "):
            user_names = name.split(" ")
            users = User.objects.filter(Q(first_name__contains=user_names[0]) & Q(last_name__contains=user_names[1]))
        else:
            users = User.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name))
        serializer = UserSearchSerializer(users, many=True)
        return Response(serializer.data)

