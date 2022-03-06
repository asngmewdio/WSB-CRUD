from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    pass

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identityNumber = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    representative = models.ForeignKey("Representative", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Representative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email