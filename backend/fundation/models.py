from django.db import models
from django.contrib.auth import get_user_model
from customaccount.accountTypes import StudentAccount,FundationStaffAccount

User = get_user_model()


class Fundation(models.Model):
    TYPES = (
        ("UNIVERSITY","University"),
        ("SCHOOL","School")
    )
    type        = models.CharField(max_length=10,choices=TYPES,default="SCHOOL")
    admin       = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name        = models.CharField(max_length=150)
    date_funded = models.DateField()
    students    = models.ManyToManyField(StudentAccount,blank=True,related_name='studentFundation')
    staff       = models.ManyToManyField(FundationStaffAccount,blank=True,related_name='staffFundation')



class FundationStaffGroup(models.Model):
    fundation   = models.ForeignKey(Fundation,on_delete=models.CASCADE,related_name="fundationStaffGroups")
    staff       = models.ManyToManyField(FundationStaffAccount)


class FundationStage(models.Model):
    fundation           = models.ForeignKey(Fundation,on_delete=models.CASCADE,related_name='fundationStages')
    name                = models.CharField(max_length=150)
    summary             = models.TextField(max_length=1000)
    admin               = models.ForeignKey(FundationStaffAccount,on_delete=models.SET_NULL,null=True)


class FundationDepartment(models.Model):
    fundation           = models.ForeignKey(Fundation,on_delete=models.CASCADE,related_name='fundationDepartments')
    name                = models.CharField(max_length=150)
    summary             = models.TextField(max_length=1000)
    studentAdmins       = models.ManyToManyField(StudentAccount,related_name='studen')
    staffAdmins         = models.ManyToManyField(FundationStaffAccount)
    students            = models.ManyToManyField(StudentAccount)
    


class FundationEvent(models.Model):
    name            = models.CharField(max_length=200)
    description     = models.TextField(max_length=1000)
    date            = models.DateField()
    time            = models.TimeField()
    location        = models.CharField(max_length=200)
    staffInvited    = models.ManyToManyField(FundationStaffAccount,related_name='staffEvents')
    studentsInvited = models.ManyToManyField(StudentAccount,related_name='studentInvites')
    lecturer        = models.ForeignKey(FundationStaffAccount,on_delete=models.SET_NULL,null=True,related_name='staffLecturer')
    aotherDetails   = models.TextField(max_length=500)
    eventGroup      = models.ManyToManyField(FundationStaffGroup,blank=True)

