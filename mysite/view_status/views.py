from django.shortcuts import render, redirect
from course_app.models import courseApplicationAllRequired

from course_app.forms import courseForm1
from django.shortcuts import redirect
from course.models import AddCourseModel
from register.models import StudentUser
from .models import *
from django.http import HttpResponse

def view_status(response, course_name, student_username, application_status):


    context = {
            'student' : student_username,
            'course' : course_name,
            'application_status': application_status,
        }

    return render(response, 'view_status.html',  {'custom_attribute': context})

def update_hire_status_accepted(request, username, course_name):

    application = courseApplicationAllRequired.objects.get(Username=username, Course_Name=course_name)
    student = StudentUser.objects.get(username=username)
    course  = AddCourseModel.objects.get(Course_Name = course_name)
    

    student.hire_status = "Hired"
    application.Application_Status = 'Accepted_by_both'
    student.save()
    application.save()
    context = {
        "course": application.Course_Name,
        "username": application.Username,
        "status": application.Application_Status
    }

    return render(request, 'view_status.html', {'custom_attribute': context})


def update_hire_status_rejected(request, username, course_name):
        application = courseApplicationAllRequired.objects.get(Username=username, Course_Name=course_name)
        student = StudentUser.objects.get(username=username)

        application.Application_Status = 'Rejected'

        application.save()
        context = {
            "course": application.Course_Name,
            "username": application.Username,
            "status": application.Application_Status
        }

        return render(request, 'view_status.html', {'custom_attribute': context})
