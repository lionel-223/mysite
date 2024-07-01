import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construction de l'email
            email_subject = f'Message de {name} via votre site 1ldmind.com'
            email_message = f'Nom: {name}\nAdresse mail: {email}\nMessage:\n{message}'

            # Envoi de l'email via SMTP
            try:
                send_mail(
                    email_subject,
                    email_message,
                    '1ldmind.com',  # From email
                    ['daviddelouest@gmail.com'],  # To email
                    fail_silently=False,
                )
            except Exception as e:
                print(f"An error occurred: {e}")

            return HttpResponseRedirect(reverse('contact:success'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

