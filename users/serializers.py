from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        max_length=227,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered."
            )
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(default=None, allow_null=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_employee = serializers.BooleanField(default=False, allow_null=True)

    def update(self, instance: User, validated_data: dict):

        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def create(self, validated_data) -> User:
        if validated_data["is_employee"]:
            validated_data["is_superuser"] = True
        else:
            validated_data["is_superuser"] = False
        create_user = User.objects.create_user(**validated_data)
        return create_user

    def __str__(self) -> str:
        return f"Name {self.username} é id: [{self.id}]"
