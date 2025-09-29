from django.urls import path
from .views import menu_items_by_category

urlpatterns = [
    path('items/', menu_items_by_category, name='menu'-items-by-category'),
]