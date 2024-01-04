from app.main.exceptions import BaseExceptionResponse
from . import env


BASE_EXCEPTION_RESPONSE = {
    422: {
        "model": BaseExceptionResponse,
        "description": "Base Exception Response"
    }
}

FASTAPI = dict(
    title=env.APP_TITLE,
    summary=env.APP_SUMMARY,
    description=env.APP_DESCRIPTION,
    version=env.APP_VERSION,
    docs_url="/",
    responses=BASE_EXCEPTION_RESPONSE
)


ENVS = [
    env.EMAIL,
    env.PASSWORD,
    env.ACCESS_KEY,
]


class Smtp:
    EMAIL = env.EMAIL
    PASSWORD = env.PASSWORD
    HOST = env.SMTP_HOST
    PORT = env.SMTP_PORT
