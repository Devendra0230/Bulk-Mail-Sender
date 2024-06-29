from celery import Celery, shared_task
from mainapp.tasks import *  
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your tasks here
from celery import shared_task

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@shared_task
def signup_otp(re_email, otp):
    # Email content
    content = f"""<h3>Verify Your Email Address for Bulk mail sender</h3>Hello {re_email}  <br>Thanks for signing up for Bulk mail sender! To complete your registration   and the features, <br> please verify your email address by entering the One-Time      Password (OTP) we sent you.<br><b>Your OTP is: {otp}</b><br>This OTP will expire   in 3 minutes.
    
Thanks,
The Bulk Mail Sender Team
    """
    from_email = "bulkmail1@geektheo.com"
    password = "bulkmail1@bulkmail1"
    subject = "Email Varification Code"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = re_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(content, "html"))

    # SMTP server configuration
    smtp_server = "mail.geektheo.com"
    smtp_port = 465
    smtp_username = from_email
    smtp_password = password

    # Create SMTP object
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(from_email, re_email, message.as_string())

    # Quit the SMTP server
    server.quit()

    print("Email sent successfully!")
    return True



@shared_task
def signup_success(email):
     # Email content
    content = f"""<h3>Your signing-up proccese is complite for Bulk mail sender</h3>Hi {email}<br>Thanks for signing up for Bulk mail sender.Your registration is successfull,<br>Your Email is your username.
    
Thanks,
The Bulk Mail Sender Team
"""
    from_email = "bulkmail1@geektheo.com"
    password = "bulkmail1@bulkmail1"
    subject = "Signup Successfully"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(content, "html"))

    # SMTP server configuration
    smtp_server = "mail.geektheo.com"
    smtp_port = 465
    smtp_username = from_email
    smtp_password = password

    # Create SMTP object
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(from_email, email, message.as_string())

    # Quit the SMTP server
    server.quit()

    print("Email sent successfully!")
    return True


@shared_task
def pass_reset_otp(email,otp):
     # Email content
    content = f"""
    <h3>Hi {email},<h3>
    <h3>Verify Your Email Address for Bulk mail sender</h3>

<p>You recently requested to reset your password for your account on Bulk mail sender.</p>
<p/><b>Please use the OTP '{otp}' to reset your password<b></p>
For security reasons, this OTP will expire in 5 minutes.

Thanks,
The Bulk Mail Sender Team

        """
    from_email = "bulkmail1@geektheo.com"
    password = "bulkmail1@bulkmail1"
    subject = "Password Reset OTP"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(content, "html"))

    # SMTP server configuration
    smtp_server = "mail.geektheo.com"
    smtp_port = 465
    smtp_username = from_email
    smtp_password = password

    # Create SMTP object
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(from_email, email, message.as_string())

    # Quit the SMTP server
    server.quit()

    print("Email sent successfully!")
    return True


