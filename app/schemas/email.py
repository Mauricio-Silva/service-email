from pydantic import BaseModel, Field
from app.utils.custom_types import (
    USERNAME_VALIDATOR,
    SUBJECT_VALIDATOR,
    EMAIL_VALIDATOR,
    URL_VALIDATOR
)


class EmailSend(BaseModel):
    to: EMAIL_VALIDATOR = Field(...)
    subject: SUBJECT_VALIDATOR = Field(...)
    username: USERNAME_VALIDATOR = Field(...)
    link: URL_VALIDATOR = Field(...)
