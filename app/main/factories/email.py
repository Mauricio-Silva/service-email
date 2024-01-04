from app.data.usecases import DbAccountConfirmation, DbResetPassword
from app.infra.smtp import SmtpService


def make_db_account_confirmation() -> DbAccountConfirmation:
    smtp_service = SmtpService()
    return DbAccountConfirmation(smtp_service)


def make_db_reset_password() -> DbResetPassword:
    smtp_service = SmtpService()
    return DbResetPassword(smtp_service)
