from django.db import models
from django.contrib.auth.models import user


# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=16)
#     nic = models.CharField(max_length=16)
#     avatar = models.FilePathField()
#     email = models.EmailField()
#     password = models.CharField(max_length=32)
#     registr_time = models.DateTimeField()


class Message(models.Model):
    text_message = models.CharField(max_length=512)
    image = models.FilePathField()
    message_time = models.DateTimeField()
    uuser = models.ForeignKey(user, on_delete=models.CASCADE)
