from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()



class FundationStaffAccount(models.Model):
    """Staff Account in a fundation
    
    This model represnts a staff role into a fundation to do certin tasks 
    With lmitied permiessions

    Args:
        user (User): the user ID for stass account : since every (user related object ) should hace a user model attached to it
        role (CharField) : staff role (every role has a limited permissions attached to this role ) 
        phoneNumber (CharField with regex ) : staff contact info
        email (EmailField) : staff contact info 
        
    """
    
    ROLES = (
        ("doctor-teacher"," مدرس - دكتور "),
        ("lecturer","محاضر"),
        ("students-ffairs","مدير شؤون الطلبة")
    )
    
    
    user                =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='fundationStaff')
    role                = models.CharField(max_length=50,choices=ROLES)
    phoneNumber         = models.CharField(max_length=10)
    email               = models.EmailField(max_length=200)
    address             = models.CharField(max_length=300)
    
    def __str__(self):
        
        return f"{self.user.first_name + ' ' + self.user.last_name} ({self.role}) "


class StudentAccount(models.Model):
    """ 
    Studetn account in a foundation
        Args:
            user (User): the user ID for student account : since every (user related object ) should hace a user model attached to it
            phoneNumber (CharField with regex ) : student contact info
            email (EmailField) : student contact info 
            fundationID (CharField): each student should have an ID in the fundation database to make sure that this student is belong to the right fundation
            address (CharField): student address
        
    """

    user                = models.ForeignKey(User,on_delete=models.CASCADE,related_name='students')
    phoneNumber         = models.CharField(max_length=10)
    address             = models.CharField(max_length=300)
    email               = models.EmailField(max_length=200)
    fundationID         = models.CharField(max_length=150,unique=True)


    def __str__(self):
        
        return f"{self.user.first_name + ' ' + self.user.last_name} ({self.fundationID})"