from django.urls import path
from . views import IndexView, ProfileView,ProfileEditView,PostProjectView
urlpatterns = [
    path('', IndexView, name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('project/create/', PostProjectView, name='project-create'),
]
