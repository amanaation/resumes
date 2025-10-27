import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()


class EmailSender:

    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.sender_email = 'iamanmishra2007@gmail.com'
        self.sender_password = 'oixa gzlm rytr hnki'

    def send(self, subject, body, body_type='html', default_txt=None, to_recipients=None, bcc_recipients=None,
             attachment_path=None):
        # Create the email
        msg = EmailMessage()
        msg['From'] = self.sender_email
        msg['Subject'] = subject

        if bcc_recipients:
            msg['Bcc'] = ', '.join(bcc_recipients)

        if to_recipients:
            msg['To'] = ', '.join(to_recipients)

        if default_txt:
            msg.set_content(default_txt)

        msg.add_alternative(body, subtype=body_type)

        if attachment_path:
            # Add the PDF file
            filename = attachment_path.split("/")[-1]
            with open(attachment_path, 'rb') as pdf_file:
                pdf_data = pdf_file.read()
                msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=filename)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)

        print("Email sent successfully to BCC recipients.")
