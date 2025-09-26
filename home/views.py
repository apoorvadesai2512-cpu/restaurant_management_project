from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from home.models import MenuCategory
from home.serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

    