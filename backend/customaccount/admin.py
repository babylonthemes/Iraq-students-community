from django.contrib import admin
from .models import CustomAccount
from .accountTypes import StudentAccount,FundationStaffAccount

admin.site.register(CustomAccount)
admin.site.register(FundationStaffAccount)
admin.site.register(StudentAccount)
