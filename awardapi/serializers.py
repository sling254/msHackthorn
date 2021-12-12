from rest_framework import serializers
from ..projects.models import Project, UserProject


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')