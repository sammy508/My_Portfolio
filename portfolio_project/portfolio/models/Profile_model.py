
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, max_length=750)
    profile_picture = models.ImageField(upload_to="Profile_Image/",blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username