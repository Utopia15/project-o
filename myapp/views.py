# myapp/views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_email = form.cleaned_data['recipient_email']

            send_mail(
                subject,
                message,
                'your-email@example.com',  # From email
                [recipient_email],  # To email
                fail_silently=False,
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})

def success(request):
    return render(request, 'success.html')
