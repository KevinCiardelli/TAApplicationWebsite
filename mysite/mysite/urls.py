"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as register_view
from login import views as login_view
from landing_page import views as landing_views
from course import views as course_views
from home_page import views as home_views
from course_app import views as course_app_views
from show_courses import views as show_courses_views
from view_applications import views as application_views
from student_view_appplications import views as student_application_views
from view_status import views as status_views
from course.views import update_status_field

from . import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Boston College TA Application'
admin.site.index_title = 'Admin Information'

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", include("main.urls")),
    path('', landing_views.landing_page, name='landing'),
    path('landing/', landing_views.landing_page, name='landing'),
    path("register/", register_view.register, name="register"),
    path("login/", login_view.login_view, name="login"),
    path('logout/', login_view.logout_view, name='logout'),
    path('course_creation/', course_views.add_course_view, name='course_creation'),
    path('edit_course/<str:course_id>/', course_views.edit_course_view, name='edit_course'),
    path('home/', home_views.home_view, name='home'),
    path('course_app/<int:course_id>/<int:current_user_id>/', course_app_views.course_app_view, name='course_app'),
    path('student_landing_page/', landing_views.student_landing_page, name="student_landing_page"),
    path('view_courses_instructor/', show_courses_views.show_courses_instructor_view, name='view_courses_instructor'),
    path('view_courses_student/', show_courses_views.show_courses_student_view, name='view_courses_student'),
    path('instructor_landing_page/', landing_views.instructor_landing_page, name='instructor_landing_page'),
    path('view_applications/<str:custom_attribute>/', application_views.view_applications, name='view_applications_list'),
    path('student_view_appplications/', student_application_views.view_applications, name='student_view_appplications'),
    path('update_status_field/<int:course_id>/', course_views.update_status_field, name='update_status_field'),
    path('update_application_status_accept/<str:username>/<str:course_name>/', course_app_views.update_application_status_accept, name='update_application_status_accept'),
    path('update_application_status_reject/<str:username>/<str:course_name>/', course_app_views.update_application_status_reject, name='update_application_status_reject'),
    path('view_status/<str:course_name>/<str:student_username>/<str:application_status>/', status_views.view_status, name='view_status'),
    path('update_hire_status_accepted/<str:username>/<str:course_name>/', status_views.update_hire_status_accepted, name='update_hire_status_accepted'),
    path('update_hire_status_rejected/<str:username>/<str:course_name>/', status_views.update_hire_status_rejected, name='update_hire_status_rejected'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

