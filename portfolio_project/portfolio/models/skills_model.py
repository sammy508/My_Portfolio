
from django.db import models
from django.contrib.auth.models import User

class SkillsModels(models.Model):

    profile = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name="skills"
    )
    name = models.CharField(null=True, blank= True, max_length=50)
    category = models.CharField(max_length=50)
    level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"