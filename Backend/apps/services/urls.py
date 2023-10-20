from django.urls import path
from .views import *
urlpatterns = [
    path('service', ListCreateView.as_view()),
    path('service/<int:pk>', RetrieveUpdateDestroyView.as_view()),
]
