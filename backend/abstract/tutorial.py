from django.db import models
from .dateAndTime import BaseDateTime


class BaseTutorial(BaseDateTime,models.Model):
    
    uploadTo            = "abstract/tutorial/%Y/%m/%d"
    title               = models.CharField(max_length=200)
    intro               = models.TextField(max_length=2000)
    thumbnail           = models.ImageField(upload_to=uploadTo)

    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        abstract = True


class BaseTutorialSection(BaseDateTime,models.Model):
    
    uploadTo            = "abstract/tutorial/sections/%Y/%m/%d"
    title               = models.CharField(max_length=150)
    content             = models.TextField(max_length=2000)
    thumbnail           = models.ImageField(upload_to=uploadTo)

    class Meta:
        abstract = True

class BaseTutorialComment(BaseDateTime,models.Model):
    
    text                = models.TextField(max_length=1000)

    class Meta:
        abstract = True