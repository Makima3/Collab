from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response 
from .serializers import ServicesSerializers
from apps.animals.serializers import AnimalSerializer 
from .models import ServiceModel


class ListCreateView(ListCreateAPIView):
    serializer_class = ServicesSerializers
    queryset = ServiceModel.objects.all()

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = ServicesSerializers
    queryset = ServiceModel.objects.all()
    def post(self, *args, **kwargs):
        service = self.get_object()
        data = self.request.data
        serializer = AnimalSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(service=service)
        
        return Response(serializer.data, status=201)
        

