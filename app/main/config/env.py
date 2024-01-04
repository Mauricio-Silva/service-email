from dotenv import load_dotenv
from os import getenv


load_dotenv()

PREFIX = "/service-email/api"
APP_TITLE = "Service-Email"
APP_VERSION = "v1.0.0"
APP_SUMMARY = "A service to manage emails"
APP_DESCRIPTION = """
<!-- cSpell:disable -->
Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso do Sul - Três Lagoas <br/>
Tecnologia em Análise e Desenvolvimento de Sistemas - TADS <br/>

**SnapCut** - Social media for sharing videos
"""

EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASSWORD")
ACCESS_KEY = getenv("ACCESS_KEY")

SMTP_HOST = getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = getenv("SMTP_PORT", 465)
