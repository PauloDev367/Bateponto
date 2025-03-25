from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import os

def clockin_image_upload_path(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    return f"clockin-submition/{unique_filename}"  

class ApplicationUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='users_images/')
    name = models.CharField(max_length=255)
    user_webapp_id = models.BigIntegerField(null=True)
    start_work_time= models.TimeField(null=True)
    end_work_time= models.TimeField(null=True)

class ClockIn(models.Model):
    user_name = models.CharField(null=True, max_length=255)
    user_email = models.EmailField(null=True)
    user_id = models.BigIntegerField(null=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    insert_method = models.CharField(max_length=255)
    foto_sended = models.ImageField(upload_to=clockin_image_upload_path, null=True)