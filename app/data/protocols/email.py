from abc import ABCMeta, abstractmethod
from pydantic import BaseModel


class SendEmailInput(BaseModel):
    to: str
    subject: str
    content: str


class SendEmailRepository(metaclass=ABCMeta):
    Input = SendEmailInput

    @abstractmethod
    def send_email(self, data: Input) -> None:
        pass
