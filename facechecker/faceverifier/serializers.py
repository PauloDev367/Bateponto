from rest_framework import serializers
from .models import ApplicationUser
from django.core.exceptions import ValidationError

class LoginSerializer(serializers.Serializer):
   email = serializers.EmailField()
   password = serializers.CharField(write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField()
    
    class Meta:
        model = ApplicationUser
        fields = ['email', 'password', 'username', 'profile_picture']
  
    def create(self, validated_data):
        user = ApplicationUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            profile_picture=validated_data['profile_picture']
        )
        return user
    
    def validate_email(self, value):
        user = ApplicationUser.objects.filter(email=value).first()
        if user:
            raise ValidationError('Este e-mail já está em uso!')
        return value