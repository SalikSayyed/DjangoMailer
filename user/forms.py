from django import forms
from mail.models import Mail 

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields  = [
            'mail_sender',
            'mail_receiver',
            'mail_subject',
            'mail_body',
            'mail_attachements',
        ]