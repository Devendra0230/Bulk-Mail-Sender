import datetime
from django import template
from user.models import receiverFileModel
from django.conf import settings
from django.core import mail


register = template.Library()


@register.simple_tag
def first():
        
        x = mail.send_mail('varification code', 'i am mahendr singh', settings.      EMAIL_HOST_USER, ['mahendrasinghstudy6977@gmail.com'], fail_silently=False)
        if x:
            return 'mail sent successfully'
        else:
              return'mail not sent'