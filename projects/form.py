from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder': 'Project title'
            }))
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'live_link','github_like']