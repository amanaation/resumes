from pprint import pprint
from utils import find_unsent_emails, update_email_list, read_body, read_default_txt
from EmailSender import EmailSender

import os
from dotenv import load_dotenv

load_dotenv()

resume_file_path = os.getenv('resume_path')
pdf_filename = os.getenv('resume_filename')


def main():
    recipients = find_unsent_emails()
    role = "gen_ai"
    # role = "data_engineer"
    html_body = read_body(role)
    default_txt = read_default_txt()

    for company in recipients:
        name = company
        print(f"Sending emails to {name}")

        if role == "gen_ai":
            subject = f'Immediate joiner for Gen AI Development/Python Development opportunities @{name.capitalize()}'
        else:
            subject = f'Immediate joiner for Data Engineer/ Python Developer/ AI Developer opportunities @{name.capitalize()}'

        bcc_recipients = list(set(recipients[name]))

        EmailSender().send(subject, body=html_body, default_txt=default_txt,
                           bcc_recipients=bcc_recipients, attachment_path=resume_file_path)

        update_email_list(name, bcc_recipients)
        print(f"Email sent successfully to BCC recipients of {name}")


if __name__ == "__main__":
    main()
    # data = dict(domain='@gmail.com', emails=['amanmishramax345@gmail.com'], name='IBM')
    # mark_sent(**data)
