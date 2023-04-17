from django.db import models
from .dateAndTime import BaseDateTime
from django.core.exceptions import ValidationError

def checkFileType(value:str):
    allowed = ['mp4','mov','wmv','avi']
    
    for format in allowed:
        if  not value.endswith(format ) or not value.endswith(format.upper):
            raise ValidationError(
            "File type  is not supported  ",
            "fileNotSupported"
            
            )


class BaseReel(BaseDateTime,models.Model):
    
    
    validators          = [checkFileType]
    uploadTo            = "videos/%Y/%m/%d"
    thumbnailUploadTo   = 'videos/%y/%m/%d/thumbnail'
    
    
    alt                 = models.CharField(max_length=150)
    video               = models.FileField(upload_to=uploadTo,validators=validators)


class BaseReelComment(BaseDateTime,models.Model):
    
    text                = models.TextField(max_length=500)