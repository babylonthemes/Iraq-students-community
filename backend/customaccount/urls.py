from django.urls import path
from .views import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'index', UsersViewSet)


