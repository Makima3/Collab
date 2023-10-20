from django.urls import path
from .views import *
urlpatterns = [
    path('animal', ListCreateView.as_view()),
    path('animal/<int:pk>', RetrieveUpdateDestroyView.as_view()),
]
