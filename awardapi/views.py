from django.shortcuts import render
from rest_framework import viewsets
from ..projects.models import Project, UserProject
from .serializers import ProjectSerializer, UserProjectSerializer
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
