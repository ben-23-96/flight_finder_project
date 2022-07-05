import smtplib
import ssl


class EmailSender:
    def __init__(self):
        self.port = 465  # For SSL
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = "testpythonsend23@gmail.com"
        self.receiver_email = None
        self.password = 'Katmando23*'

    def send_email(self, email_message, recipient):
        message = email_message
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, recipient, message)
