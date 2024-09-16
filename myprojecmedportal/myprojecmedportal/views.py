# views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_email_view(request):
    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['chillamichael15@gmail.com-email@example.com'] 

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {e}')
