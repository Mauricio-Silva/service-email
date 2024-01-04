from abc import ABCMeta, abstractmethod
from pydantic import BaseModel


class EmailInput(BaseModel):
    to: str
    subject: str
    username: str
    link: str


class AccountConfirmation(metaclass=ABCMeta):
    Input = EmailInput

    @abstractmethod
    def send(self, data: Input) -> None:
        pass


class ResetPassword(metaclass=ABCMeta):
    Input = EmailInput

    @abstractmethod
    def send(self, data: Input) -> None:
        pass
