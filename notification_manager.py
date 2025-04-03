from twilio.rest import Client
import os 
from dotenv import load_dotenv
import smtplib 
load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
class NotificationManager:
    def __init__(self):
        self.account_sid = account_sid
        self.auth_token = auth_token


    def sendmessage(self, smsbody):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(

            from_ ='+18038849786',
            body=smsbody,
            to='+923084581471'
        )
        print(message.sid)

    def sendmail(self, mailbody , rec_email):
        
        email = your email here
        
        password = your code here

        with  smtplib.SMTP("smtp.gmail.com" , 587) as f:
            f.starttls()
            f.login(user = email , password = password )
            f.sendmail(from_addr=email , to_addrs=rec_email, msg = mailbody)
            print("message sent")
            print(rec_email)

