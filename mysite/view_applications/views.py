from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.utils import send_email

from course_app.models import courseApplicationAllRequired

from register.models import StudentUser
from django.contrib.auth.models import User

# Create your views here.

def view_applications(request, custom_attribute):
    unhired_users = StudentUser.objects.filter(hire_status = 'unhired')
    unhired_users = [user.username for user in unhired_users]
    current_user = request.user
    # get applications with file 
    application_list_1 =  courseApplicationAllRequired.objects.all()
    application_list_2 = application_list_1.filter(Course_Name=custom_attribute)
    application_list_3 = application_list_2.filter(Username__in=unhired_users)
    
    
    # append sets
    combined_applications = application_list_3
    
    return render(request, 'view_applications.html', {'custom_attribute': combined_applications})
