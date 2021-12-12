from django.shortcuts import render
from rest_framework import viewsets
from projects.models import Project, UserProfile
from .serializers import ProjectSerializer, UserProfileSerializer
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer