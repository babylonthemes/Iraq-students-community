from django.db import models
from .managers import Manager
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from django.contrib.auth.hashers import make_password
import datetime

class CustomAccount(AbstractBaseUser,PermissionsMixin):
    username            = models.CharField(max_length=50,unique=True,help_text=None)
    email               = models.EmailField(verbose_name=' الايميل  ',unique=True,blank=False,null=True,help_text=None)
    first_name          = models.CharField(max_length=30,verbose_name=' الاسم الاول  ',blank=False,null=False,default='',help_text=None)
    last_name           = models.CharField(max_length=30,verbose_name=' الاسم الاخير  ',blank=False,null=False,default='',help_text=None)
    is_admin            = models.BooleanField(default=False,verbose_name=' مسؤل موقع  ',help_text=None)
    is_superuser        = models.BooleanField(default=False,verbose_name='  مدير ')
    is_active           = models.BooleanField(default=True,verbose_name=' فعال ',help_text=None)
    is_staff            = models.BooleanField(default=False,verbose_name=' موظف  ',help_text=None)
    date_joined         = models.DateTimeField(auto_now=True,help_text=None)
    gender              = models.CharField(max_length=120,choices=(('female','انثى '),('male','ذكر '),),default='male')
    has_mark            = models.BooleanField(default=False)
    verified            = models.BooleanField(default=False)
    is_developer        = models.BooleanField(default=False)
    policy              = models.BooleanField(default=False,blank=False)



    
    objects = Manager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    class Meta:
        db_table = 'account'
        verbose_name_plural = 'المستخدمين '



    def __str__(self):
        return str(self.id)





    def change_first_name(self,name):
        self.first_name = name
        self.save()
        
    def tokens(self):
        return f"{self.first_name},{self.last_name},{self.username},{self.email}"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.last_password_change_attemp = datetime.datetime.now()
        self.save()




