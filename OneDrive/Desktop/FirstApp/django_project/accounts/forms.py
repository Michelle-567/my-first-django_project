from django import forms
from django.contrib.auth.models import User
from .models import Application, AcademicQualification, PresentPositionInfo, Tenure, Specialization,Registration,CourseRegistration,OtherTraining
from .models import StatementOfApplicant
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class LoginForm(forms.Form):
     username = forms.CharField()
    #  email= forms.EmailField()
     password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput)


    agree_to_terms = forms.BooleanField(
        required=True,
        label='I agree to the Terms of Use and Privacy Policy',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken. Please choose a different one.')
        return username


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['specialization']  # Include only the specialization field


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['is_existing_member']  

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['user']

class AcademicQualificationForm(forms.ModelForm):
    class Meta:
        model = AcademicQualification
        fields = ['institution_name', 'date_from', 'date_to', 'course_duration', 'achievement', 'certificate', 'testimonials']


class PresentPositionInfoForm(forms.ModelForm):
    class Meta:
        model = PresentPositionInfo
        fields = ['brief_description', 'any_other_specify', 'tenure_years', 'tenure_months']

    
class MemberTypeForm(forms.Form):
    YEARS_OF_EXPERIENCE_CHOICES = [
        ('0', 'Student Member (0 years)'),
        ('0', 'Affiliate Member (Graduated and 0 years)'),
        ('1', 'Associate Member (1-2 years)'),
        ('3', 'Full Member (3 years)'),
    ]

    years_of_experience = forms.ChoiceField(
        label="Years of Experience in Relevant Quality-Related Field",
        choices=YEARS_OF_EXPERIENCE_CHOICES,
        widget=forms.RadioSelect
)


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['specialization']
        exclude = ['user']


class TenureForm(forms.ModelForm):
    class Meta:
        model = Tenure
        # fields = ['name_of_organization', 'date_from', 'date_to']
        exclude = ['user']

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ['course_name', 'course_duration', 'organization', 'achievement', 'testimonials']



class OtherTrainingForm(forms.ModelForm):
    class Meta:
        model = OtherTraining
        fields = ['course_training', 'course_duration', 'organization', 'achievement', 'testimonials']

class StatementOfApplicantForm(forms.ModelForm):
    class Meta:
        model = StatementOfApplicant
        fields = ['statement']


# class MembershipCardForm(forms.ModelForm):
#     class Meta:
#         model = MembershipCard
        # fields = ['membership_number', 'expiration_date', ...]  








