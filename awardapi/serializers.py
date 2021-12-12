from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'live_link', 'github_link', 'created_on')