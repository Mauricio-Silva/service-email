import ssl
import smtplib
from app.config.config import Config
from email.message import EmailMessage

class Email():

    def __init__(self, to, subject, username, link) -> None:
        self.to = to
        self.subject = subject
        self.username = username
        self.link = link

    
    def send_email(self, type_email):
        configs = Config()
        context = ssl.create_default_context()
    
        if type_email == "account_confirmation":
            with open('app/template/account_confirmation.html', 'r') as file:
                html_content = file.read()
            html_content = html_content.replace("{{username}}", self.username).replace('{{link}}', self.link)
        
        if type_email == "reset_password":
            with open('app/template/reset_password.html', 'r') as file:
                html_content = file.read()
            html_content = html_content.replace('{{link}}', self.link)

        en = EmailMessage()
        en['From'] = configs.EMAIL
        en['To'] = self.to
        en['Subject'] = self.subject
        en.set_content(html_content, subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(configs.EMAIL, configs.PASSWORD)
            smtp.sendmail(configs.EMAIL, self.to, en.as_string())