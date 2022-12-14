from rest_framework import serializers
from .models import Message, Friend
from api.models import User

class MessageSerializer(serializers.Serializer):
    from_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=False)
    to_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=False)
    message = serializers.CharField(required=True)
    data_dodania = serializers.DateTimeField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance

class MessageCreateSerializer(serializers.Serializer):
    to_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=False)
    message = serializers.CharField(required=True)

    def create(self, request, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.to_id = validated_data.get('to_id', instance.to_id)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance

class FriendSerializer(serializers.Serializer):
    friend1 = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=False)
    friend2 = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=False)

    def create(self, validated_data):
        return Friend.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.friend1 = validated_data.get('friend1', instance.friend1)
        instance.friend2 = validated_data.get('friend2', instance.friend2)
        instance.save()
        return instance

class FriendCreateSerializer(serializers.Serializer):
    friend2 = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=False)

    def create(self, validated_data):
        return Friend.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.friend2 = validated_data.get('friend2', instance.friend2)
        instance.save()
        return instance