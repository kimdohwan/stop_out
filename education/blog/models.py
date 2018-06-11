from django.db import models
from django.conf import settings
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)


class Student(models.Model):
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(models.DateTimeField(auto_now_add=True))
    school = models.CharField(max_length=20)
