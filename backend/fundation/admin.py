from django.contrib import admin
from .models import Fundation,FundationDepartment,FundationEvent,FundationStaffGroup,FundationStage

admin.site.register(Fundation)
admin.site.register(FundationStage)
admin.site.register(FundationDepartment)
admin.site.register(FundationEvent)
admin.site.register(FundationStaffGroup)

