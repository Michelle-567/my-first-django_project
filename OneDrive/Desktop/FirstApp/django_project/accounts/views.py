from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import MemberTypeForm, ApplicationForm, AcademicQualificationForm,  SpecializationForm, TenureForm, PresentPositionInfoForm
from .forms import LoginForm
from .forms import RegistrationForm
from .forms import CourseRegistrationForm
from .forms import UserRegistrationForm
from .forms import OtherTrainingForm
from .forms import StatementOfApplicantForm
from django.contrib.auth.decorators import login_required 
from .forms import UserProfileForm

@login_required
def index(request):
    return render(request, 'pages/index.html')


def begin_application(request):
    # Your logic for handling the beginning of the application process
    # ...

    return render(request, 'accounts/begin_application.html')  # Render the application form page


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                auth_login(request, user)
                # Redirect to a success page or any other page
                return redirect('index')
            else:
                # Handle invalid login (e.g., show an error message)
                return render(request, 'accounts/pages-login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()

    return render(request, 'accounts/pages-login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/pages-register.html', {'form': form})

@login_required
def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate with the logged-in user
            user_profile.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserProfileForm()

    return render(request, 'pages/users-profile.html', {'form': form})

def logout(request):
  logout(request)
  return redirect('/accounts/login')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user  # Set the user field
            form.save()  # Save the data to the database
            return redirect('success_page')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'accounts/registration_form.html', {'form': form})

def member_type_view(request):
    if request.method == 'POST':
        form = MemberTypeForm(request.POST)
        if form.is_valid():
            # years_of_experience = form.cleaned_data.get('years_of_experience')
            
            # Now you can associate this information with the logged-in user
            # request.user.profile.years_of_experience = years_of_experience
            # request.user.profile.save()

            # Redirect to a success page or another appropriate response
            messages.success(request, "send")
            return redirect('application')
    else:
        form = MemberTypeForm()

    return render(request, 'accounts/membertype_form.html', {'form': form})

def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('academic_qualification')
    else:
        form = ApplicationForm()

    return render(request, 'accounts/application_form.html', {'form': form})
@login_required
def academic_qualification_view(request):
    if request.method == 'POST':
        form = AcademicQualificationForm(request.POST, request.FILES)
        if form.is_valid():
            academic_qualification = form.save(commit=False)
            academic_qualification.user = request.user
            academic_qualification.save()
            return redirect('present_position')  # Redirect to a success page
    else:
        form = AcademicQualificationForm()

    return render(request, 'accounts/academicqualification_form.html', {'form': form})


def present_position_info_view(request):
    if request.method == 'POST':
        form = PresentPositionInfoForm(request.POST)
        if form.is_valid():
            present_position_info = form.save(commit=False)
            present_position_info.user = request.user  # Associate with the logged-in user
            present_position_info.save()
            return redirect('specialization')  # Redirect to a success page
    else:
        form = PresentPositionInfoForm()

    return render(request, 'accounts/present_position_info_form.html', {'form': form})

def specialization_view(request):
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            specialization = form.save(commit=False)
            specialization.user = request.user  # Associate with the logged-in user
            specialization.save()
            return redirect('tenure')  # Redirect to a success page
    else:
        form = SpecializationForm()

    return render(request, 'accounts/specialization_form.html', {'form': form})

def success_page(request):
    return render(request, 'accounts/success_page.html')

def tenure_form(request):
    if request.method == 'POST':
        form = TenureForm(request.POST)
        if form.is_valid():
            tenure = form.save(commit=False)
            tenure.user = request.user
            tenure.save()
            return redirect('courses')  # Replace 'success_page' with the appropriate URL
    else:
        form = TenureForm()

    return render(request, 'accounts/tenure_form.html', {'form': form})

def course_registration(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('other_training')  # Replace 'success_page' with the appropriate URL
    else:
        form = CourseRegistrationForm()

    return render(request, 'accounts/courses_form.html', {'form': form})

def other_training_view(request):
    if request.method == 'POST':
        form = OtherTrainingForm(request.POST, request.FILES)
        if form.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            training.save()
            return redirect('statement_form')  # Replace 'success_page' with the appropriate URL
    else:
        form = OtherTrainingForm()

    return render(request, 'accounts/other_training_form.html', {'form': form})


@login_required
def statement_of_applicant(request):
    if request.method == 'POST':
        form = StatementOfApplicantForm(request.POST)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.user = request.user
            statement.save()
            return redirect('success_page')  # Redirect to a success page or another view
    else:
        form = StatementOfApplicantForm()
                   
    return render(request, 'accounts/statement_form.html', {'form': form})

