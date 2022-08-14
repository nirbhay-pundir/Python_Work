from auth import main
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

service = main()


def create_message(service, to, subject, message):
    emailMsg = message
    Message = MIMEMultipart()
    Message['to'] = to
    Message['subject'] = subject
    Message.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(Message.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    return message


print(create_message(service, 'gmail.com', 'Test email', 'This is a simple test email'))
