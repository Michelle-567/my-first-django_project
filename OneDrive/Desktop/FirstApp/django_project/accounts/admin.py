from django.contrib import admin
from .models import Application
from .models import AcademicQualification
from .models import Registration
from .models import Specialization


# Register the Application model
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', )  # Customize displayed fields

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization')
    # list_filter = ('specialization',)
    # search_fields = ('user__username', 'specialization')
    # list_per_page = 20

admin.site.register(Specialization)



admin.site.register(AcademicQualification)   

admin.site.register(Registration)

from .models import Tenure

class TenureAdmin(admin.ModelAdmin):
    list_display = ('name_of_organization', 'date_from', 'date_to')

admin.site.register(Tenure)


from .models import OtherTraining

class OtherTrainingAdmin(admin.ModelAdmin):
    list_display = ('course_training', 'course_duration', 'organization', 'achievement')

admin.site.register(OtherTraining)


from .models import StatementOfApplicant 

class ApplicantStatementAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date', 'statement_checkbox']
  
admin.register(StatementOfApplicant)

