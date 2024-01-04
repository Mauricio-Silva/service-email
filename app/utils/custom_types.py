from typing import Annotated
from pydantic import constr


USERNAME_REGEX = r"^[a-zA-Z0-9_]+$"
EMAIL_REGEX = r"^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
URL_REGEX = r"^(https?|ftp):\/\/[^\s\$.?#].[^\s]*$"


USERNAME_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=6,
    max_length=12,
    pattern=USERNAME_REGEX
)]

EMAIL_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=7,
    max_length=70,
    pattern=EMAIL_REGEX
)]

SUBJECT_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=3,
    max_length=70,
    # pattern=NAME_REGEX
)]

URL_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    pattern=URL_REGEX
)]
