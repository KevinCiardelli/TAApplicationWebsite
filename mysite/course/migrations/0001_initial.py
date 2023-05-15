from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(blank=True, max_length=100)),
                ('Course_ID', models.CharField(blank=True, max_length=100)),
                ('Section', models.CharField(blank=True, max_length=10)),
                ('Marking_Meetings', models.CharField(blank=True, max_length=10)),
                ('Lecture_Times', models.DateTimeField(blank=True, null=True)),
                ('Discussion_Times', models.DateTimeField(blank=True, null=True)),
                ('Course_Description', models.TextField(blank=True)),
                ('Office_Hours_per_week', models.PositiveIntegerField(blank=True, null=True)),
                ('Instructor', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
