from django.urls import path
from . views import IndexView, ProfileView,ProfileEditView,PostProjectView, ProjectEditView
urlpatterns = [
    path('', IndexView, name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('project/edit/<int:pk>/', ProjectEditView.as_view(), name='project-edit'),
    path('project/create/', PostProjectView, name='project-create'),
]
