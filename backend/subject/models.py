from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    SUBJECT_TYPE = (
        ("SCIENTIFIC","Scientific"),
        ("LITERARY","Literary")
    )
    by                  = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name                = models.CharField(max_length=150,unique=True)
    date                = models.DateField()
    time                = models.TimeField()

    
    def __str__(self) -> str:
        return self.name