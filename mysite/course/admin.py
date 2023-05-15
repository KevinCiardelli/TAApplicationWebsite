from django.contrib import admin
from .models import AddCourseModel
from .forms import AddCourseForm


class CustomCourseAdmin(admin.ModelAdmin):
    form = AddCourseForm
    readonly_fields = ('Instructor_Name', 'Instructor_ID', 'Status')
    list_display = ('Course_Name', 'Course_ID', 'Section', 'Marking_Meetings', 'Resume_Required', 'Cover_Letter', 'References', 'Office_Hours_per_week', 'TA_Positions', 'Lecture_Days', 'Lecture_Times', 'Discussion_Days', 'Discussion_Times', 'Course_Description')


admin.site.register(AddCourseModel)

# Register your models here.
