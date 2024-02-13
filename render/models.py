from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.BigIntegerField()
    avatar = models.FilePathField()
    name = models.CharField(max_length=16)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    registr_time = models.DateTimeField()


class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # - ?
    #user = models.CharField(max_length=16)
    id = models.BigIntegerField()
    text_message = models.CharField(max_length=512)
    image = models.FilePathField()
    message_time = models.DateTimeField()
