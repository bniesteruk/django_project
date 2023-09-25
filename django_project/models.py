from django.db import models
from .models import SomeModel

class SomeModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField()