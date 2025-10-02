

# This view is created for template of Django in another view you can get API and you can implement them where you want

from django.shortcuts import render, get_object_or_404
from portfolio.models import Profile
from portfolio.models.education_models import Education
from portfolio.models.projects_models import ProjectModel
from portfolio.models.skills_model import SkillsModels
from portfolio.models.certification_model import CertificateModel

# -------------------------
# Home / Portfolio Page
# -------------------------
def home(request):
    profile = Profile.objects.first()  # single-user
    education = Education.objects.all()
    skills = SkillsModels.objects.all()
    projects = ProjectModel.objects.all()
    certificates = CertificateModel.objects.all()

    context = {
        "profile": profile,
        "education": education,
        "skills": skills,
        "projects": projects,
        "certificates": certificates,
    }
    return render(request, "portfolio/home.html", context)


# -------------------------
# Optional separate pages
# -------------------------
def skills_page(request):
    skills = SkillsModels.objects.all()
    return render(request, "portfolio/skills.html", {"skills": skills})


def education_page(request):
    education = Education.objects.all()
    return render(request, "portfolio/education.html", {"education": education})


def projects_page(request):
    projects = ProjectModel.objects.all()
    return render(request, "portfolio/projects.html", {"projects": projects})


def certificates_page(request):
    certificates = CertificateModel.objects.all()
    return render(request, "portfolio/certificates.html", {"certificates": certificates})
