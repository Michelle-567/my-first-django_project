from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('begin_application/', views.begin_application, name='begin_application'),   
    path('pages-login.html/', views.login_view, name='login'),
    path('pages-register.html/', views.register, name='register'),  

    path('users-profile.html/', views.user_profile_view, name='user_profile'),
    path('logout.html/', auth_views.LogoutView.as_view(), name='logout'),


    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

   #pasword reset
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('registration_form.html/', views.registration_view, name='registration'),
    path('membertype_form.html/',views.member_type_view, name='membertype'),
    path('application_form.html/', views.application_view, name='application'),
    path('academicqualification_form.html/', views.academic_qualification_view, name='academic_qualification'),
    path('present-position-info_form.html/', views.present_position_info_view, name='present_position'),
    

    path('specialization_form.html/', views.specialization_view, name='specialization'),
    path('success_page.html/', views.success_page, name='success_page'), 
    path('tenure_form.html/', views.tenure_form, name='tenure'),
    path('course_registration_form.html/', views.course_registration, name='courses'),
    path('other_training_form.html/', views.other_training_view, name='other_training'),
    path('statement_form.html/', views.statement_of_applicant, name='statement_form'),
    
   
]






    





    

