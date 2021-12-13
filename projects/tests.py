# Create your tests here.
from django.test import TestCase
from .models import Rate,Project,UserProfile
from django.contrib.auth.models import User


class RateTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='testuser')
    self.project = Project.objects.create(id=1, title='Moringa Project', description='Moringa Project description',created_on='2021,12,19',image='https://cloudinary url', github_link='http://github.com',live_link='http://heroku.com',user=self.user)
    self.rating = Rate.objects.create(id=1, design_wise=5, usability_wise=8, content_wise=6, user=self.user, project=self.project)

  def test_instance(self):
    self.assertTrue(isinstance(self.rating, Rate))

  def test_save_rating(self):
    self.rating.save_rating()
    rating = Rate.objects.all()
    self.assertTrue(len(rating) > 0)

  def test_get_ratings(self, id):
    self.rating.save()
    rating = Rate.get_ratings(post_id=id)
    self.assertTrue(len(rating) == 1)

class TestUserProfile(TestCase):
  def setUp(self):
    self.user = User(id=1, username='testuser', password='Moringa')
    self.user.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()

class ProjectTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='Moringa')
    self.project = Project.objects.create(id=1, title='Moringa Project', description='Moringa Project description',created_on='2021,12,19',image='https://cloudinary url', github_link='http://github.com',live_link='http://heroku.com',user=self.user)

  def test_instance(self):
    self.assertTrue(isinstance(self.project, Project))

  def test_display_projects(self):
    self.project.save()
    projects = Project.all_projects()
    self.assertTrue(len(projects) > 0)

  def test_save_post(self):
    self.project.save_project()
    project = Project.objects.all()
    self.assertTrue(len(project) > 0)

  def test_delete_post(self):
    self.project.delete_project()
    project = Project.search_project('another_project')
    self.assertTrue(len(project) < 1)

  def test_search_projects(self):
    self.project.save()
    project = Project.search_project('another_project')
    self.assertTrue(len(project) > 0)