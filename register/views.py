from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponseRedirect,HttpResponse
from .forms import LoginForm
from mail.models import Mail as ml
from user.models import User as us
from django.contrib.auth.models import User as uss
from django.template import loader
from django.contrib import messages

# Create your views here.
def user_register(request):
    form = UserForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('login')

        
    context ={
        'form':form
    }
    return render(request,"user_register.html",context)
def user_login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data['email'])
            try:
                email_context = us.objects.get(email=form.cleaned_data['email'])
            except:
                print("Not right no move forward!")
                return render(request, 'login_form.html', {'form': form})
            if email_context:
                print("email not matched")
                # email_context = us.objects.get(email=form.cleaned_data['email'])
                print(email_context.email)
                if email_context.password == form.cleaned_data['password']:
                    print("Password  matches")
                    c={
                    'mail_received' : email_context.mail_received,
                    'mail_sent': email_context.mail_sent,
                    }
                    template = loader.get_template("user_inbox.html")
                    messages.add_message(request, messages.INFO, form.cleaned_data['email'])
                    return HttpResponseRedirect('user_inbox')
                    return HttpResponse(template.render(c,request))
            print("Not right!")
            return render(request, 'login_form.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {'form': form})