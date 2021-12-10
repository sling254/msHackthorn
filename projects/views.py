from django.shortcuts import render
from django.views import View
from .models import UserProfile


# Create your views here.


def IndexView(request):
    return render(request, 'index.html')


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'profile.html', context)
