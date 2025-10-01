


from rest_framework import serializers
from ..models.Profile_model import Profile
from .education_serializer import EducationSerializer

class ProfileSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True) 
    

    class Meta:
        model = Profile
        fields ='__all__'