from django.contrib.auth.models import AbstractUser
from django.db import models

class ApplicationUser(AbstractUser):
    profile_picture = models.ImageField()
    name = models.CharField(max_length=255)