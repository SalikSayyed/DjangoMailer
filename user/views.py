from django.shortcuts import render
from .forms import MailForm
from django.contrib import messages
from mail.models import Mail as ml
from user.models import User as us
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def actual_send(secretinfo):
    return
def try_again(request):
    return render(request,"tryagain.html")
def mail_sender_form(request):
    data = {
        'mail_sender' : request.session['email'],
    }
    form = MailForm(request.POST or None, request.FILES,initial=data)
    if form.is_valid():
        form.cleaned_data['email'] = request.session['email']
        backend = EmailBackend(
            host='smtp.gmail.com',
            port = 587,
            username = request.session['email'],
            password = us.objects.get(email=request.session['email']).password,
            use_tls = True,
            fail_sliently=False,
            )
        email = EmailMessage(
            subject = form.cleaned_data['mail_subject'],
            body = form.cleaned_data['mail_body'],
            from_email = request.session['email'],
            to = (form.cleaned_data['mail_receiver'],),
            connection=backend,
        )
        try:
            email.send()
            form.save()
            c = { 'status' : "Success"}
            return render(request,'mail_status.html',c)
        except:
            c = { 'status' : "Failure"}
            return render(request,'mail_status.html',c)
    context ={
        'form':form,
        'email':request.session['email'],
    }
    return render(request,"userlogged.html",context)
def user_inbox(request):
    storage = messages.get_messages(request)
    edmail = None
    for message in storage:
        edmail = message
    email_context = us.objects.get(email=edmail)
    c={
        'mail_received' : email_context.mail_received,
        'mail_sent': email_context.mail_sent,
    }
    request.session['email'] = email_context.email
    return render(request,"user_inbox.html",c)
def home(request):
    context={
        'hello':'hi'
    }
    return render(request,"base.html",context)

