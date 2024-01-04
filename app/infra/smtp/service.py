from app.data.protocols import SendEmailRepository
from app.main.exceptions import FailedDependency
from email.message import EmailMessage
from ssl import create_default_context
from app.utils.logger import Logger
from app.main.config import Smtp
from smtplib import SMTP_SSL


class SmtpService(SendEmailRepository):
    SUBTYPE = "html"
    FROM_FIELD = "From"
    TO_FIELD = "To"
    SUBJECT_FIELD = "Subject"

    def send_email(self, data: SendEmailRepository.Input) -> None:
        context = create_default_context()

        email_message = EmailMessage()
        email_message[self.FROM_FIELD] = Smtp.EMAIL
        email_message[self.TO_FIELD] = data.to
        email_message[self.SUBJECT_FIELD] = data.subject
        email_message.set_content(data.content, subtype=self.SUBTYPE)

        try:
            with SMTP_SSL(Smtp.HOST, Smtp.PORT, context=context) as smtp:
                smtp.login(Smtp.EMAIL, Smtp.PASSWORD)
                try:
                    smtp.sendmail(Smtp.EMAIL, data.to, email_message.as_string())
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
