from dotenv import load_dotenv
from os import getenv

load_dotenv()

APP_PORT = getenv('APP_PORT')
EMAIL= getenv('EMAIL')
PASSWORD= getenv('PASSWORD')

