import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(email, licencekey):
    # Email content
    content = f"""Licence key = {licencekey}"""
    from_email = "bulkmail1@geektheo.com"
    password = "bulkmail1@bulkmail1"
    subject = "Licence Key"

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

# Example usage
sendmail("simpleboykrishna0@gmail.com", "testlicencekey")
