
from django.contrib.auth.models import BaseUserManager

class Manager(BaseUserManager):

    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError(' user must have email  ')
        if not username:
            raise ValueError(' user must have username  ')
        

        user = self.model(
            email=email,
            username=username            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user






    def create_superuser(self,username,email,password=None):
        user = self.create_user(username=username,email=email,password=password)
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_developer = True
        user.save(using=self._db)
        return user

