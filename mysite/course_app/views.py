from django.shortcuts import render, redirect
from mysite.utils import send_email
from .forms import *
from course.models import AddCourseModel
from register.models import StudentUser
from .models import *
from django.http import HttpResponse
from django.contrib import messages


def course_app_view(response, course_id, current_user_id):

    data = AddCourseModel.objects.get(id=course_id)
    student = StudentUser.objects.get(id=current_user_id)
    Course_Name = data.Course_Name
    Course_Section = data.Section
    Username= response.user.username

    if courseApplicationAllRequired.objects.filter(Username=Username, Course_Name=Course_Name).exists():
        return HttpResponse('You have already applied to this course!')

    if(student.app_counter > 4):
        return HttpResponse('You have applied to the maximum amount of applications!')


    form = courseForm1()
    if response.POST:
        form = courseForm1(response.POST, response.FILES)
        if form.is_valid() and response.FILES:

            application = form.save(commit=False)
            application.Course_Name = Course_Name
            application.Section = Course_Section
            application.Application_Status = "Pending"
            application.Username = Username
            student.app_counter+=1
            application.save()
            student.save()
            return redirect('student_landing_page')

    else:
        form = courseForm1()

    context = {
        'student' : student,
        'course' : data,
        'Username' : Username,
        'form' : form
    }

    return render(response, 'course_app_page.html', context)


def update_application_status_accept(request, username, course_name):
    application = courseApplicationAllRequired.objects.get(Username=username, Course_Name=course_name)
    student = StudentUser.objects.get(username=username)

    application.Application_Status = "Accepted"
    application.save()
    message = "Congratulations "+username+", you have been selected to TA for "+course_name +"! Check your account."
    subject = "Boston College TA Application Status Update"
    send_email(student.email, subject, message)
    application_list_1 =  courseApplicationAllRequired.objects.all()
    application_list_1 = application_list_1.filter(Course_Name=course_name)

    return render(request, 'view_applications.html', {'custom_attribute': application_list_1})



def update_application_status_reject(request, username, course_name):
    application = courseApplicationAllRequired.objects.get(Username=username, Course_Name=course_name)
    student = StudentUser.objects.get(username=username)

    application.Application_Status = "Rejected"
    application.save()
    message = "Unfortunately "+username+", you have not been selected to TA for "+course_name +" Check your account."
    subject = "Boston College TA Application Status Update"
    send_email(student.email, subject, message)
    application_list_1 =  courseApplicationAllRequired.objects.all()
    application_list_1 = application_list_1.filter(Course_Name=course_name)
    student.app_counter-=1
    student.save()

    return render(request, 'view_applications.html', {'custom_attribute': application_list_1})
