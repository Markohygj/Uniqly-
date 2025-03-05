

from django.db import models

from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Користувач'),
        ('moderator', 'Модератор'),
        ('admin', 'Адміністратор'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to="Image", null= True)
    hat = models.ImageField(upload_to="Image",null=True)




