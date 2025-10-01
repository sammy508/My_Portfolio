
from rest_framework import generics
from portfolio.models import Profile
from portfolio.serializers import ProfileSerializer

class SingleProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        # always return the first profile (single-user portfolio)
        profile = Profile.objects.first()
        if not profile:
            raise Profile.DoesNotExist("Profile not found")
        return profile