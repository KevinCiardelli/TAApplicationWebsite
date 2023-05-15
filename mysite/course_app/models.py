import uuid
from django.db import models

class courseApplicationAllRequired(models.Model):
    COURSE1 = "Monday 6-6:50"
    COURSE2= "Tuesday 6-6:50"
    COURSE3= "Wednesday 2-2:50"
    Course_Name = models.CharField(max_length=100, editable=False)
    Course_Section = models.CharField(max_length=100, editable=False)
    Course_Choices = [(COURSE1,"Monday 6-6:50"), (COURSE2, "Tuesday 6-6:50"), (COURSE3, "Wednesday 2-2:50")]
    Discussion_Time_1 = models.CharField(max_length=100, blank=False)
    Discussion_Time_2 = models.CharField(max_length=100, blank=False)
    First_and_Last_Name = models.CharField(max_length=100, blank=False)
    Username = models.CharField(max_length=100, editable=False)
    Resume = models.FileField(upload_to='course_app/resumes/', blank=False)
    Anything_you_want_to_add  = models.CharField(max_length=500, blank=True, default='')
    Application_Status = models.CharField(max_length=100, editable=False, default='')

