from rest_framework import serializers
from projects.models import Project,UserProfile


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'live_link', 'github_link', 'created_on')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'bio', 'birth_date','picture', 'location','email','picture')