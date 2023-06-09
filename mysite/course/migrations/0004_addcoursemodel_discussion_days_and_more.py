# Generated by Django 4.1.7 on 2023-04-02 22:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_addcoursemodel_ta_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcoursemodel',
            name='Discussion_Days',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=3),
        ),
        migrations.AddField(
            model_name='addcoursemodel',
            name='Instructor_ID',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='addcoursemodel',
            name='Lecture_Days',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=3),
        ),
        migrations.AlterField(
            model_name='addcoursemodel',
            name='Discussion_Times',
            field=models.DurationField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='addcoursemodel',
            name='Lecture_Times',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='addcoursemodel',
            name='Marking_Meetings',
            field=models.BooleanField(blank=True, max_length=10),
        ),
    ]
