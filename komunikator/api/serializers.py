from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        def create(self, validate_data):
            return User.objects.create(**validate_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.native_name = validated_data.get('native_name', instance.native_name)
            instance.phone_no = validated_data.get('phone_no', instance.phone_no)
            instance.save()
            return instance

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
        ]


