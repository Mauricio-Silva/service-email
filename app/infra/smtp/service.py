from app.data.protocols import SendEmailRepository
from app.main.exceptions import FailedDependency
from email.mime.multipart import MIMEMultipart
from ssl import create_default_context
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from app.utils.logger import Logger
from app.main.config import Smtp
from smtplib import SMTP_SSL


class SmtpService(SendEmailRepository):
    IMAGE_PATH = "app/infra/templates/logo.png"
    MODE = "rb"
    SUBTYPE = "html"
    FROM_FIELD = "From"
    TO_FIELD = "To"
    SUBJECT_FIELD = "Subject"
    HEADER_NAME = "Content-ID"
    HEADER_VALUE = "<logo>"

    def send_email(self, data: SendEmailRepository.Input) -> None:
        context = create_default_context()

        message = MIMEMultipart()
        message[self.FROM_FIELD] = Smtp.EMAIL
        message[self.TO_FIELD] = data.to
        message[self.SUBJECT_FIELD] = data.subject

        body = MIMEText(data.content, self.SUBTYPE)
        message.attach(body)

        with open(self.IMAGE_PATH, self.MODE) as file:
            image = MIMEImage(file.read())
            image.add_header(self.HEADER_NAME, self.HEADER_VALUE)
            message.attach(image)

        try:
            with SMTP_SSL(Smtp.HOST, Smtp.PORT, context=context) as smtp:
                smtp.login(Smtp.EMAIL, Smtp.PASSWORD)
                try:
                    smtp.sendmail(Smtp.EMAIL, data.to, message.as_string())
                except Exception:
                    raise FailedDependency("Error in sending Email")
        except Exception:
            message = "Cannot connect to SMTP server"
            Logger.error(message)
            raise FailedDependency(message)

    @classmethod
    def check_connection(cls):
        context = create_default_context()
        try:
            with SMTP_SSL(Smtp.HOST, Smtp.PORT, context=context) as smtp:
                try:
                    smtp.login(Smtp.EMAIL, Smtp.PASSWORD)
                except Exception:
                    raise FailedDependency("Cannot login in SMTP server")
        except Exception:
            message = "Cannot connect to SMTP server"
            Logger.error(message)
            raise FailedDependency(message)
