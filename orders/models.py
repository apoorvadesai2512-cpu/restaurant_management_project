from django.db import models

# Create your models here.
from home.models import OrderStatus

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name