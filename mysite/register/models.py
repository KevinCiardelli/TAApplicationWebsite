from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import  Group, Permission


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    app_counter = models.PositiveIntegerField(default=0)

    hire_status = models.CharField(max_length=7, default='unhired')

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="custom_users_groups",  # specify a unique related_name
        related_query_name="custom_user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="custom_users_permissions",  # specify a unique related_name
        related_query_name="custom_user",
    )
    

class StudentUser(CustomUser):
    class Meta:
        proxy = True
