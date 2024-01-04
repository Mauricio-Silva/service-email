from starlette.responses import Response
from typing import Callable, Awaitable
from pydantic import BaseModel
from fastapi import Request


CALL_NEXT_RESPONSE = Callable[[Request], Awaitable[Response]]


class BaseResponse(BaseModel):
    message: str
    success: bool = True


class MessageResponse(BaseResponse):
    pass
