from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AnimalSerializer
from .models import AnimalModel


class ListCreateView(ListAPIView):
    serializer_class = AnimalSerializer
    queryset = AnimalModel.objects.all()

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = AnimalModel.objects.all()