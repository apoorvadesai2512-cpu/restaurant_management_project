from rest_framework import serializers
from home.models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'description', 'is_available', 'category']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("price must be a positive number.")
        return value