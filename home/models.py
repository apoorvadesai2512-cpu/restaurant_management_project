from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.charField(max_length=100, unique=True)

    def __str__(self):
        return self.name
        