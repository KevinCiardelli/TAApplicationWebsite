# Generated by Django 4.1.7 on 2023-05-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseapplicationallrequired',
            name='Discussion_Time_1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courseapplicationallrequired',
            name='Discussion_Time_2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courseapplicationallrequired',
            name='Username',
            field=models.CharField(max_length=100),
        ),
    ]