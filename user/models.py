from django.db import models
from mail.models import Mail

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=50)
    details = models.TextField()
    @property
    def mail_received(self):
        return Mail.objects.filter(mail_receiver=self.email)
    @property
    def mail_sent(self):
        return Mail.objects.filter(mail_sender=self.email)

