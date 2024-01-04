from app.infra.smtp import SmtpService
from contextlib import asynccontextmanager
from app.main.config import ENVS
from fastapi import FastAPI
from .logger import Logger


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not all(ENVS):
        message = "Environment Variables must be specified"
        Logger.error(message)
        raise ValueError(message)
    SmtpService.check_connection()
    Logger.info("\033[33mConnected to the SMTP Email Server\033[m")
    yield
