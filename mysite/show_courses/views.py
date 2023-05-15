
#views
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import ToDoList, Item
#from .forms import CreateNewList
# Create your views here.
from course.models import AddCourseModel

# Create your views here.

##show_courses will show course, course ID, and 2 buttons: view apps + edit courses
def show_courses_instructor_view(request):
    current_user = request.user
    course_list = AddCourseModel.objects.all()
    course_list = course_list.filter(Instructor_Name=current_user)
    context = {
        'course_list' : course_list
    }
    return render(request, 'show_courses_instructor_view.html', context)
# Create your views here.

#this view below has been added such that students see the apply button
##instead of the edit courses/ view applications buttons

def show_courses_student_view(request):
    course_list = AddCourseModel.objects.all()
    current_user = request.user.username
    current_user_id = request.user.id
    print(current_user_id)
    context = {
        'current_user_id' : current_user_id,
        'current_user' : current_user,
        'course_list' : course_list
    }
    return render(request, 'show_courses_student_view.html', context)
