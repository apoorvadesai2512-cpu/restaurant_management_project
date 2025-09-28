from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from home.models import MenuItem
from home.serializers import MenuItemSerializer
from rest_framework.pagination import PageNumberPagination

class MenuItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MenuItemSearchViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = MenuItemSerializer
    pagination_class = MenuItemPagination

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset
        

    