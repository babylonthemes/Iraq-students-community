from django.db import models
from django.contrib.auth.models import Permission

class Role(models.Model):
    code_name = models.CharField(max_length=150,unique=True)
    role_name = models.CharField(max_length=150)
    permissions = models.ManyToManyField(Permission,blank=False)
    