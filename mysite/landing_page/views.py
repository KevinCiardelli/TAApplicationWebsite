from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing.html')

@login_required
def student_landing_page(request):
    context = {'user': request.user}
    return render(request, 'student_landing_page.html', context)

@login_required
def instructor_landing_page(request):
    context = {'user': request.user}
    return render(request, 'instructor_landing_page.html', context)