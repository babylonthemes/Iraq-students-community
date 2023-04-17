from django.db import models
from .dateAndTime import BaseDateTime

class Group(BaseDateTime,models.Moodel):
    
    uploadTo            = "abstract/group/%Y/%m/%d"
    name                = models.CharField(max_length=300)
    descripton          = models.TextField(max_length=1000)
    thumbnail           = models.ImageField(upload_to=uploadTo)
    cover               = models.ImageField(upload_to=uploadTo)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True


class BaseGroupRole(BaseDateTime,models.Model):
    
    role                = models.CharField(max_length=150)


