from django.db import models

# Create your models here.
class Mail(models.Model):
    mail_sender = models.EmailField()
    mail_receiver = models.EmailField()
    mail_subject = models.TextField(default='No Subject Mail',null=True,blank=True)
    mail_body = models.TextField(default='--empty--',null=True,blank=True)
    mail_attachements = models.FileField(null=True,blank=True)