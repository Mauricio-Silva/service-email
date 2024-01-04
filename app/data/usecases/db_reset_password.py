from app.domain.usecases import ResetPassword
from app.data.protocols import SendEmailRepository


class DbResetPassword(ResetPassword):
    TEMPLATE_PATH = "app/infra/templates/reset_password.html"
    LINK = "{{link}}"

    def __init__(
        self,
        send_email_repository: SendEmailRepository
    ) -> None:
        self.__send_email_repository = send_email_repository

    def send(self, data: ResetPassword.Input) -> None:
        with open(self.TEMPLATE_PATH) as file:
            html_content = file.read()
        content = html_content.replace(self.LINK, data.link)

        email_data = SendEmailRepository.Input(
            to=data.to,
            subject=data.subject,
            content=content
        )
        self.__send_email_repository.send_email(email_data)
