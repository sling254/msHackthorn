from django.urls import path
from . views import IndexView, ProfileView
urlpatterns = [
    path('', IndexView, name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
