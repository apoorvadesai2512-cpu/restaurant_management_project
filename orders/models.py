from django.db import models

# Create your models here.
class Coupon(models.Model):

    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
        