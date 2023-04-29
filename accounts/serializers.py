from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if 'info' in value:
        raise serializers.ValidationError('error`s in email')


# class UserRegisterSerializers(serializers.Serializer):
#     username = serializers.CharField(max_length=35, required=True)
#     email =serializers.EmailField(required=True, validators=[clean_email])
#     password = serializers.CharField(max_length=16, required=True, write_only=True)
#     password2 = serializers.CharField(max_length=16, required=True, write_only=True)


class UserRegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=16, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)}
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('error`s in password')
        return data

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('error`s')
        if 'a' in value:
            raise serializers.ValidationError('error`s in a')
        return value

