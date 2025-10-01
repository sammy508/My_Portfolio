
from rest_framework import generics
from portfolio.models import Profile
from portfolio.serializers import ProfileSerializer
from portfolio.serializers.education_serializer import EducationSerializer
from portfolio.serializers.project_serializer import ProjectSerializer
from portfolio.serializers.skills_serializer import SkillSerializer
from ..serializers.certificate_serializer import CertificateSerializer

from ..models.education_models import Education
from ..models.projects_models import ProjectModel
from ..models.skills_model import SkillsModels
from ..models.certification_model import CertificateModel

class SingleProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        # always return the first profile (single-user portfolio)
        profile = Profile.objects.first()
        if not profile:
            raise Profile.DoesNotExist("Profile not found")
        return profile
    



class SkillView(generics.RetrieveAPIView):
    serializer_class = SkillSerializer

    def get_object(self):
        # always return the first profile (single-user portfolio)
        skills = SkillsModels.objects.first()
        if not skills:
            raise SkillsModels.DoesNotExist("Skills not found")
        return skills
    

class EducationView(generics.RetrieveAPIView):
    serializer_class = EducationSerializer

    def get_object(self):
        # always return the first profile (single-user portfolio)
        education = Education.objects.first()
        if not education:
            raise Education.DoesNotExist("Education not found")
        return education
    

class ProjectsView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer

    def get_object(self):
        # always return the first profile (single-user portfolio)
        projects = ProjectModel.objects.first()
        if not projects:
            raise ProjectModel.DoesNotExist("Projects not found")
        return projects
    


class CertificatesView(generics.RetrieveAPIView):
    serializer_class = CertificateSerializer

    def get_object(self):
        # always return the first profile (single-user portfolio)
        certificate = CertificateModel.objects.first()
        if not certificate:
            raise CertificateModel.DoesNotExist("certificate not found")
        return certificate
    



    



