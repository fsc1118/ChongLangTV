from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16, default="Unspecified")
    password = models.CharField(max_length=16, default="Unspecified")
    isAdministrator = models.BooleanField(default=False)


class Course(models.Model):
    courseName = models.CharField(max_length=16, default="Unspecified")
