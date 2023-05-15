from django.contrib import admin
from .forms import *
from .models import *


class CustomCourseAdmin1(admin.ModelAdmin):
    form = courseForm1
    readonly_fields = ('Course_Name','Course_Section', 'Application_Status', 'Username')
    list_display = ('Course_Name', 'Course_Section', 'Discussion_Time_1', 'Discussion_Time_2', 'First_and_Last_Name', 'Resume', 'Anything_you_want_to_add')


admin.site.register(courseApplicationAllRequired, CustomCourseAdmin1)
