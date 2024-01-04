from app.main.dependencies import RequestBody, AccessKey
from app.schemas.common import MessageResponse
from app.schemas.email import EmailSend
from fastapi.routing import APIRouter
from app.main.config import PREFIX
from fastapi import Body, Depends
from app.main.factories import (
    make_db_account_confirmation,
    make_db_reset_password
)
from typing import Annotated


router = APIRouter(prefix=f"{PREFIX}/email", tags=["Email"])


@router.post(
    "/account_confirmation",
    status_code=200,
    summary="Send a Email for Account confirmation",
    response_description="Confirming the Account",
    response_model=MessageResponse,
    dependencies=[
        Depends(AccessKey()),
        Depends(RequestBody())
    ]
)
async def account_confirmation(data: Annotated[EmailSend, Body()]):
    db_account_confirmation = make_db_account_confirmation()
    db_account_confirmation.send(data)

    return MessageResponse(message="Account confirmation Email successfully sent")


@router.post(
    "/reset_password",
    status_code=200,
    summary="Send a Email to Reset Password",
    response_description="Reseting the Password",
    response_model=MessageResponse,
    dependencies=[
        Depends(AccessKey()),
        Depends(RequestBody())
    ]
)
async def reset_password(data: Annotated[EmailSend, Body()]):
    db_reset_password = make_db_reset_password()
    db_reset_password.send(data)

    return MessageResponse(message="Reset password Email successfully sent")
