"""MailingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from user.views import mail_sender_form
from user.views import home
from register.views import user_register
from register.views import user_login
from user.views import user_inbox

urlpatterns = [
    path('',home),
    path('mailsender/',mail_sender_form),
    path('admin/', admin.site.urls),
    path('register/',user_register),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',user_login),
    path('register/login',user_login),
    path('login/user_inbox/',user_inbox),

]
