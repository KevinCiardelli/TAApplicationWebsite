# Generated by Django 4.1.7 on 2023-03-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_customuser_groups_alter_customuser_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor'), ('admin', 'Admin')], max_length=20),
        ),
    ]
