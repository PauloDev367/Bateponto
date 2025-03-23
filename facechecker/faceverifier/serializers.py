from rest_framework import serializers
from .models import ApplicationUser
from django.core.exceptions import ValidationError
import uuid
from slugify import slugify
from .services.facechecker import FaceCheck

def unique_image_name(instance, filename):
    ext = filename.split('.')[-1]
    return f"profile_pictures/{uuid.uuid4()}.{ext}"

class LoginSerializer(serializers.Serializer):
   email = serializers.EmailField()
   password = serializers.CharField(write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField()
    
    class Meta:
        model = ApplicationUser
        fields = ['email', 'password', 'name', 'profile_picture', 'user_webapp_id']
  
    def create(self, validated_data):
        faceCheck =FaceCheck()
        
        verification = faceCheck.verificar_rosto(validated_data['profile_picture'])
        if verification is None:
            profile_picture = validated_data.pop('profile_picture', None)
            
            
            user = ApplicationUser.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                username=f"{uuid.uuid4()}_{slugify(validated_data['name'])}",
                name=validated_data['name'],
                user_webapp_id=validated_data['user_webapp_id']
            )

            if profile_picture:
                profile_picture.name = unique_image_name(user, profile_picture.name)
                user.profile_picture = profile_picture
                user.save()

            return user
        raise ValidationError('Este rosto já está cadastrado no nosso sistema!')
    
    def validate_email(self, value):
        user = ApplicationUser.objects.filter(email=value).first()
        if user:
            raise ValidationError('Este e-mail já está em uso!')
        return value


class CheckUserImageSerializer(serializers.Serializer):
    profile_picture = serializers.ImageField()
    
    class Meta:
        fields = ['profile_picture']