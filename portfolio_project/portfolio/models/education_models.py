
from django.db import models
from .Profile_model import Profile


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="educations")
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True, null=True)  # e.g., BSc, MSc
    field_of_study = models.CharField(max_length=255, blank=True, null=True)  # e.g., Computer Science
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null if ongoing
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_date"]  # newest first

    def __str__(self):
        return f"{self.school} - {self.degree or ''}"