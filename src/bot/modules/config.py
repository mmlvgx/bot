from os import environ
from dotenv import load_dotenv


load_dotenv()


class Config:
    TOKEN: str = environ.get('token')
