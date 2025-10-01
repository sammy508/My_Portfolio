



from rest_framework import serializers

from ..models.skills_model import SkillsModels


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsModels
        fields = "__all__"