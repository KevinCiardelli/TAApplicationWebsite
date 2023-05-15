from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from django.contrib import messages
from mysite.utils import send_email
from django.contrib.auth.models import User

# Create your views here.

def register(response):
    #form = registerForm()
    #form = UserCreationForm()

    if response.method == "POST":
        #form = registerForm(response.POST)
        #form = UserCreationForm(response.POST)
        form = CustomUserCreationForm(response.POST)
        if form.is_valid():
            form.save()

            # create user
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username, email=email, password=password)

            #confirm user creation
            messages.success(response, f'Account created for {username}!')

            # Send account creation email
            message = "Congratulations "+username+", your account with the TA System has been successuly created!"
            subject = "Boston College TA System Account Creation"
            send_email(form.cleaned_data.get('email'), subject, message)

            role = form.cleaned_data.get('role')

            # set admin as suoeruser
            if role == 'admin':
                user.is_superuser = True
                user.is_staff = True
                
            if role == 'student':
                user.app_counter = 0
                user.hired_status = "unhired"

            #save user
            user.save()
            return redirect ('landing')

    else:

        form = CustomUserCreationForm()
    return render(response, "register/register.html", {"form": form})
