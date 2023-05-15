from django.db import models
from django.contrib.auth.backends import BaseBackend
from register.models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
