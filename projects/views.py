from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import UserProfile, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# Create your views here.


def IndexView(request):
    projects = Project.objects.all().order_by('-date_created')
    
    context = {
        "projects": projects,
    }
    return render(request, 'index.html', context)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
        

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False