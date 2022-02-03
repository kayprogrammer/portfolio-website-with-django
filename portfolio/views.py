from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

import sweetify
import threading
from . models import *
# Create your views here.

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    
    def run(self):
        self.email.send()

def send_mail(request):
    email_subject = request.POST.get('subject')
    email_body = render_to_string('portfolio/email_body.html', {
        'name':request.POST.get('name'), 
        'email': request.POST.get('email'),
        'message': request.POST.get('message')
    })

    email = EmailMessage(subject = email_subject, body=email_body, from_email = settings.EMAIL_FROM_USER,
    to = ['kayprogrammer1@gmail.com']
    
    )

    EmailThread(email).start()

def handler404(request, exception=None):
    sweetify.error(request, title='Sorry', text='That page you were looking for does not exist', icon='error', button='Ok', timer=4000)
    return redirect('/')

def handler500(request):
    sweetify.error(request, title='Sorry', text='Something went wrong, Try again later', icon='error', button='Ok', timer=4000)
    return redirect('/')

def home(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    works = Work.objects.all().order_by('date_created')

    portfolios = Portfolio.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(request)
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        sweetify.success(request, title='Success', text='Your message has been received. We\'ll get back to you shortly', icon='success', button='Ok', timer=4000)
        return redirect('/')
    context = {'about':about, 'skills':skills, 'works':works, 'portfolios':portfolios}
    return render(request, 'portfolio/index.html', context)