# Generated by Django 4.1.7 on 2023-05-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_alter_courseapplicationallrequired_anything_you_want_to_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseapplicationallrequired',
            name='Application_Status',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
    ]
