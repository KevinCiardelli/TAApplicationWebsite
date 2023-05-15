from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER

def send_email(to_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )
