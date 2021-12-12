from django.urls import path
from . views import IndexView, ProfileView,ProfileEditView,PostProjectView, ProjectEditView,DetailView,ProjectSearch
urlpatterns = [
    path('', IndexView, name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('project/edit/<int:pk>/', ProjectEditView.as_view(), name='project-edit'),
    path('project/create/', PostProjectView, name='project-create'),
    path('project/detail/<int:project_id>/',DetailView,  name='project-detail'),
    path('project/search/',ProjectSearch.as_view(),  name='project-search'),
]
