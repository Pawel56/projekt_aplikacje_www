from rest_framework import serializers
from .models import Message
from api.models import User

class MessageSrializer(serializers.Serializer):
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