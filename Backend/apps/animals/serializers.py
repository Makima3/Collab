from rest_framework.serializers import ModelSerializer
from .models import AnimalModel

class AnimalSerializer(ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = ('id', 'type_animal')
    