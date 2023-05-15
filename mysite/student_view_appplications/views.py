from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import ToDoList, Item
#from .forms import CreateNewList
# Create your views here.
from course_app.models import courseApplicationAllRequired
from register.models import StudentUser

# Create your views here.

def view_applications(request):
    current_user = request.user.username
    
    # get applications with file 
    application_list_1 =  courseApplicationAllRequired.objects.all()
    application_list_1 = application_list_1.filter(Username=current_user)
    applications = [] 
    
    # if student is hired, only show positioned application
    for application in application_list_1:
        if application.Application_Status == "Accepted_by_both":
            applications.append(application)
            return render(request, 'student_view_applications.html', {'custom_attribute': applications})
    
    # otherwise show all applications    
    return render(request, 'student_view_applications.html', {'custom_attribute': application_list_1})
            
