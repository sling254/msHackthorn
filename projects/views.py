from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import UserProfile, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .form import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def IndexView(request):
    projects = Project.objects.all().order_by('-created_on')
    
    context = {
        "projects": projects,
    }
    return render(request, 'index.html', context)
@login_required
def PostProjectView(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)      
            form.user = request.user
            form.save()
            return redirect('index')

    else:
        form = ProjectForm()

    return render(request,'post_project.html',{"form":form})
    
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