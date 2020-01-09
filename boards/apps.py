from django.apps import AppConfig
from decouple import config

class BoardsConfig(AppConfig):
    name = 'boards'

SECRET_KEY = config('SECRET_KEY')