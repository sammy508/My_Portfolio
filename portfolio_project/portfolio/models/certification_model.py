
from django.db import models
from .Profile_model import Profile


class CertificateModel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="certifications")
    name = models.CharField(max_length=150, null=True)
    issuer = models.CharField(max_length=150)
    issue_date = models.DateField()
    credential_url  = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name