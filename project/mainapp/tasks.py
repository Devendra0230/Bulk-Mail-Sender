from celery import Celery, shared_task
from django.core.exceptions import *
from mainapp.tasks import *  
from django.conf import settings
from time import sleep
from django.core.mail import send_mail

# Create your tasks here
from celery import shared_task

app = Celery('tasks', broker='pyamqp://guest@localhost//')



@shared_task
def bulk_mail_sender(context):
      sender =  context[0]
      recipients = context[1]
      subject =    context[2]
      message =    context[3]
      number =int(context[4])
      task_name = context[5]
      wrong_recipients = list(context[6])
      esp = context[7]
      port = int(context[8])
      success_recipient = []
      failed_sender = []
      index = 0
      
      for username, password in sender.items():
            settings.EMAIL_HOST = esp
            if port == 465:
                  settings.EMAIL_USE_SSL = True
                  settings.EMAIL_USE_TLS = False
            settings.EMAIL_HOST_USER = username
            settings.EMAIL_HOST_PASSWORD = password
           
            for i in range(0,number):
                  try:
                        send_mail(subject, message, settings.EMAIL_HOST_USER,[recipients[index]], fail_silently=False, html_message=message)
                        success_recipient.append(recipients[index])
                        index += 1
                  except Exception.SMTPRecipientsRefused:
                        wrong_recipients.append(recipients[index])
                        index += 1


                  except Exception as e:
                        failed_sender.append(username)
                        print(e)
                        break
                  if index == len(recipients):
                        content = [sender, recipients, wrong_recipients, failed_sender,success_recipient, task_name]
                        return content





@shared_task
def add(x,y):
      sleep(10)
      return x+y