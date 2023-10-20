from django.db import models
from core.models import BaseModel


class ServiceModel(BaseModel):
    class Meta:
        db_table = 'service'
    title = models.CharField(max_length=45)
    description = models.TextField()
    price = models.FloatField()
    
