from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
DAYS_OF_WEEK = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    )
OPTIONS = (('required', 'Required'),
           ('optional', 'Optional'),
           )
YES_NO = (('yes', 'Yes'),
           ('no', 'No'),
           )

class AddCourseModel(models.Model):
    Instructor_Name = models.CharField(max_length=100, editable=False)
    Status = models.CharField(max_length=100, editable=False)
    Instructor_ID = models.CharField(max_length=10, blank=False)
    Course_Name = models.CharField(max_length=100, blank=True)
    Course_ID = models.CharField(max_length=100, blank=True)
    Section = models.PositiveIntegerField(blank=True, null=True)
    

    Marking_Meetings = models.CharField(choices=YES_NO, max_length=15, blank= True)

    Office_Hours_per_week = models.PositiveIntegerField(blank=True, null=True)
    TA_Positions = models.PositiveIntegerField(blank=True, null=True)

    Lecture_Days = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=5, max_length=100, blank= True)
    Lecture_Times= models.CharField(max_length=20, blank=True)
    Discussion_Days = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=5, max_length=100, blank= True)
    Discussion_Times = models.CharField(max_length=20, blank=True)
    Course_Description = models.TextField(blank=True)



    # def __str__(self):
    #     return self.name
