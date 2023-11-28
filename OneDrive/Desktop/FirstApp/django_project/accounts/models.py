from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    TYPE_CHOICES = (
        ('new', 'New Member'),
        ('existing', 'Existing Member'),
    )

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_existing_member = models.CharField(max_length=10, choices=TYPE_CHOICES)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    years_of_experience = models.CharField(
        max_length=1,  # You can adjust the max_length
        choices=[
            ('0', 'Student Member (0 years)'),
            ('0', 'Affiliate Member (Graduated and 0 years)'),
            ('1', 'Associate Member (1-2 years)'),
            ('3', 'Full Member (3 years)'),
        ]
    )

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other fields for your application model
    
class AcademicQualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    course_duration = models.CharField(max_length=50)
    achievement = models.CharField(max_length=100)
    certificate = models.FileField(upload_to='certificates/')
    testimonials = models.TextField()

    def get_user(self):
        return self.user

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)  # You can change the max length as need

class PresentPositionInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brief_description = models.TextField()
    any_other_specify = models.TextField()
    tenure_years = models.PositiveIntegerField()
    tenure_months = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user',)



# SPECIALIZATION_CHOICES = [
#     ('trainer', 'Trainer'),
#     ('auditor', 'Auditor'),
#     ('assessor', 'Assessor'),
#     ('implementor', 'Implementor'),
#     ('management_representative', 'Management Representative'),
#     ('process_owner', 'Process Owner'),
#     ('quality_improvement_team_member', 'Member of Quality Improvement Team'),
#     ('quality_assurance_manager', 'Quality Assurance Manager'),
# ]
# class Specialization(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  
#     specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)

#     def __str__(self):
#         return f"{self.user.username}'s specialization: {self.specialization}"


SPECIALIZATION_CHOICES = [
    ('trainer', 'Trainer'),
    ('auditor', 'Auditor'),
    ('assessor', 'Assessor'),
    ('implementor', 'Implementor'),
    ('management_representative', 'Management Representative'),
    ('process_owner', 'Process Owner'),
    ('quality_improvement_team_member', 'Member of Quality Improvement Team'),
    ('quality_assurance_manager', 'Quality Assurance Manager'),
]

class Specialization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s specialization: {self.specialization}"


class Tenure(models.Model):
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_organization = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()


class CourseRegistration(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    achievement = models.CharField(max_length=100)
    testimonials = models.TextField()
    

    def __str__(self):
        return self.course_name
 
class OtherTraining(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_training = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    achievement = models.FileField(max_length=100)
    testimonials = models.TextField()

    def __str__(self):
        return self.course_training
    
class StatementOfApplicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    statement = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# class MembershipApplication(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#     membership_type = models.CharField(max_length=20)
#     total_payment = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_status = models.BooleanField(default=False)

    


