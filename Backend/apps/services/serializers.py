from rest_framework.serializers import ModelSerializer
from .models import ServiceModel
from apps.animals.serializers import AnimalSerializer


class ServicesSerializers(ModelSerializer):
    animal = AnimalSerializer(read_only = True, many=True)
    class Meta:
        model = ServiceModel
        fields = ('id', 'title', 'description', 'price', 'animal')
