import social_core.backends.email
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'From Prosnjit Localhost'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = 'Thnaks!!!'
        confirm_text = 'Thanks for the message. We will get right back to you.'
        context = {
            'titile': title,
            'confirm_text': confirm_text,
        }
    #context = locals()
    template = 'profiles/contact.html'
    return render(request, template, context)