from operator import mod
from django.db import models


class FirstApp(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)