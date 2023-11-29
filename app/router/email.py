from fastapi.routing import APIRouter
from typing import Annotated
from fastapi import Body
from app.model.email import Email
from app.schema.email import EmailDTO

router = APIRouter(prefix='/email')


@router.post('/account_confirmation')
async def send_email(data: EmailDTO):
    print(data)
    Email(data.to, data.subject, data.username, data.link).send_email('account_confirmation')
    return {'message': 'Email enviado com sucesso', 'success': True}


@router.post('/reset_password')
async def reset_password(data: EmailDTO):
    Email(data.to, data.subject, data.username, data.link).send_email('reset_password')
    return {'message': 'Email enviado com sucesso', 'success': True}