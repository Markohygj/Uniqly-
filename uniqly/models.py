from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Post(models.Model):
    content = models.TextField(default=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField(upload_to="Image", null= True, blank=True)


class Massage(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_massages')
    whom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='whom_massages')
