from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16, default="Unspecified")
    password = models.CharField(max_length=16, default="Unspecified")
