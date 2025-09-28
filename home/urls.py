from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import MenuItemSearchViewSet

router = DefaultRouter()
router.register(r'menu-item', MenuItemSearchViewSet, basename='menuitem-search')

urlpatterns = [
    path('', include(router.urls)),
]
