from django.db import models

# Create your models here.
from home.models import OrderStatus

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __sef__(self):
        return f"Order {self.id} - {self.customer_name}"