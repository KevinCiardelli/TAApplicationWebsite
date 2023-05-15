from django import forms
from .models import AddCourseModel

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourseModel
        fields = ['Course_Name', 'Course_ID', 'Section', 'Marking_Meetings', 'Office_Hours_per_week', 'TA_Positions', 'Lecture_Days', 'Lecture_Times', 'Discussion_Days', 'Discussion_Times', 'Course_Description']
