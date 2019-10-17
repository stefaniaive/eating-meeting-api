import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class EmailSES(object):
    AWS_REGION = "us-east-1"
    client = boto3.client('ses', region_name=AWS_REGION,
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

    SENDER = "Eating Meeting <stefaniaive@gmail.com>"
    def build_email(self, email_from, first_name, last_name, date, restaurant_id):
        # This address must be verified with Amazon SES. So I will use mine. But here should be something like invitation@eating-meeting.com

        # is still in the sandbox, this address must be verified. I will always use mine too for this trial. If you use any other the email won't be sent.
        RECIPIENT = email_from

        # The subject line for the email.
        SUBJECT = "You have a new eating meeting invitation!"

        # The HTML body of the email.
        BODY_HTML = """\
        <html>
        <head></head>
        <body>
        <h1>Hello %s %s!</h1>
            <p>You have a new meeting!</p> 
            <p> When ? %s </p>
            <p> Where? At restaurant %s </p>
        </body>
        </html>
        """ % (first_name, last_name, str(date), restaurant_id)

        CHARSET = "utf-8"

        msg = MIMEMultipart('mixed')
        # Add subject, from and to lines.
        msg['Subject'] = SUBJECT
        msg['From'] = self.SENDER
        msg['To'] = RECIPIENT

        msg_body = MIMEMultipart('alternative')
        htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
        msg_body.attach(htmlpart)

        # Attach the multipart/alternative child container to the multipart/mixed
        # parent container.
        msg.attach(msg_body)

        print(msg)

        return msg

    def send_email(self, recipient, msg):
        try:
            # Provide the contents of the email.
            response = self.client.send_raw_email(
                Source=self.SENDER,
                Destinations=[
                    recipient
                ],
                RawMessage={
                    'Data': msg.as_string(),
                },
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

emailing = EmailSES()