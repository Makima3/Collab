from django.db import models
from core.models import BaseModel
from apps.services.models  import ServiceModel
class AnimalModel(BaseModel):
    class Meta:
        db_table = 'animal'
    type_animal = models.CharField(max_length=25)
    service = models.ForeignKey(ServiceModel, on_delete=models.PROTECT, related_name='animal')