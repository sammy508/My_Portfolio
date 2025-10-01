



from rest_framework import serializers
from ..models.certification_model import CertificateModel


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateModel
        fields = "__all__"