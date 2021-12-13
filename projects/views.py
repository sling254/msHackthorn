from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import UserProfile, Project,Rate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.http import Http404,HttpResponseRedirect
from .form import ProjectForm, RatingsForm
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

class ProjectEditView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['title', 'description', 'image', 'live_link', 'github_link']
    template_name = 'project_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('project', kwargs={'pk': pk})
        

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

def DetailViews(request,project_id):
  current_user = request.user
  all_ratings = Rate.objects.filter(project_id=project_id).all()
  project = Project.objects.get(pk = project_id)
  ratings = Rate.objects.filter(user=request.user,project=project_id).first()
  rating_status = None
  if ratings is None:
    rating_status = False
  else:
    rating_status = True
  if request.method == 'POST':
    form = RatingsForm(request.POST)
    if form.is_valid():
      rate = form.save(commit=False)
      rate.user = request.user
      rate.project = project
      rate.save()
      post_ratings = Rate.objects.filter(project=project_id)

      design_ratings = [design.design_wise for design in post_ratings]
      design_wise_average = sum(design_ratings) / len(design_ratings)

      usability_ratings = [usability.usability_wise for usability in post_ratings]
      usability_wise_average = sum(usability_ratings) / len(usability_ratings)

      content_ratings = [content.content_wise for content in post_ratings]
      content_wise_average = sum(content_ratings) / len(content_ratings)

      aggregate_average_rate = (design_wise_average + usability_wise_average + content_wise_average) / 3
      print(aggregate_average_rate)
      rate.design_wise_average = round(design_wise_average, 2)
      rate.usability_wise_average = round(usability_wise_average, 2)
      rate.content_wise_average = round(content_wise_average, 2)
      rate.aggregate_average_rate = round(aggregate_average_rate, 2)
      rate.save()
      return HttpResponseRedirect(request.path_info)
  else:
      form = RatingsForm()

  context = {
      'current_user':current_user,
      'all_ratings':all_ratings,
      'project':project,
      'rating_form': form,
      'rating_status': rating_status

  }
  return render(request, 'project_details.html', context)



class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        projects = Project.objects.filter(user=profile.user).all()
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
            'projects': projects,
        }

        return render(request, 'profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = UserProfile
    fields = ['username', 'email', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
        

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False



class ProjectSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        project_list = Project.search_projects(query)

        context = {
            'project_list': project_list,
        }

        return render(request, 'search.html', context)
        