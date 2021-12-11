from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder': 'Project title'
            }))
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Short description',
            'class': 'Form-Control mt-2',
            'rows': '5',
        }))
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'live_link','github_link']