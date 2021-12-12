from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
   
]
