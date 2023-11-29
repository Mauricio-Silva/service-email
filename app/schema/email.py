from pydantic import BaseModel, Field
from app.utils.custom_types import USERNAME_VALIDATOR, EMAIL_VALIDATOR, SUBJECT_VALIDATOR, URL_VALIDATOR

class EmailDTO(BaseModel):
    to: EMAIL_VALIDATOR | None = Field(default=None)
    subject: SUBJECT_VALIDATOR | None = Field(default=None)
    username: USERNAME_VALIDATOR | None = Field(default=None)   
    link: URL_VALIDATOR | None = Field(default=None)