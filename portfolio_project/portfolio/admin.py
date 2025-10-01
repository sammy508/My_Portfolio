from django.contrib import admin
from .models.education_models import Education
from .models.Profile_model import Profile
from .models.skills_model import SkillsModels
from .models.projects_models import ProjectModel
from .models.certification_model import CertificateModel

# Register your models here.

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(SkillsModels)
admin.site.register(ProjectModel)
admin.site.register(CertificateModel)
