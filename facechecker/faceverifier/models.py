from django.contrib.auth.models import AbstractUser
from django.db import models

class ApplicationUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='users_images/')
    name = models.CharField(max_length=255)