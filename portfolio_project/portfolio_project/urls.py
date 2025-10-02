"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from portfolio.views.data_views import SingleProfileView,SkillView,EducationView,ProjectsView,CertificatesView


# For apis

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # path("profile/", SingleProfileView.as_view(), name="single-profile"),
#     # path("skills/", SkillView.as_view(), name="single-profile"),
#     # path("education/", EducationView.as_view(), name="single-profile"),
#     # path("projects/", ProjectsView.as_view(), name="single-profile"),
#     # path("certificate/", CertificatesView.as_view(), name="single-profile"),
# ]




from portfolio.views import portfolio_view  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_view.home, name='home'),  # Portfolio homepage
    path('skills/', portfolio_view.skills_page, name='skills'),
    path('education/', portfolio_view.education_page, name='education'),
    path('projects/', portfolio_view.projects_page, name='projects'),
    path('certificates/', portfolio_view.certificates_page, name='certificates'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)