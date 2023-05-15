from django.shortcuts import render, redirect
from .forms import AddCourseForm
from .models import AddCourseModel
from course.models import AddCourseModel
# Create your views here.

def add_course_view(request):

    Instructor_Name = request.user.username
    Instructor_ID = request.user.id
    form = AddCourseForm(request.POST or None)
    if form.is_valid():
        application = form.save(commit=False)
        application.Status = "Open"
        application.Instructor_Name = Instructor_Name
        application.Instructor_ID = Instructor_ID
        application.save()
        form = AddCourseForm()
        return redirect('view_courses_instructor')

    context = {
        'form' : form
    }

    return render(request, 'course_creation.html', {'form': form})

def update_status_field(request, course_id):

    data = AddCourseModel.objects.get(id=course_id)


    if data.Status == "Open":
        data.Status = "Closed"
    else:
        data.Status = "Open"
    data.save()
    return redirect('view_courses_instructor')

def edit_course_view(response, course_id):
    Instructor_Name = response.user.username
    Instructor_ID = response.user.id
    data = AddCourseModel.objects.get(Course_ID=course_id)
    form = AddCourseForm()
    if response.POST:
        form = AddCourseForm(response.POST, instance=data)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.Instructor_Name = Instructor_Name
            edit.Instructor_ID = Instructor_ID
            edit.save()
            return redirect('view_courses_instructor')

    else:
        form = AddCourseForm(instance=data)

    context = {
        'course' : data,
        'form' : form
    }

    return render(response, 'edit_course.html', context)
