
from django.db import models
from django.contrib.auth.models import User
from ..models.Profile_model import Profile

class ProjectModel(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)

    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image= models.ImageField(upload_to="ProjectsImage/", blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    technologies = models.CharField(max_length=200, blank=True, null=True)  # optional comma-separated


    def __str__(self):
        return self.title