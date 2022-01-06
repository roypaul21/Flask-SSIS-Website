from os import getenv
SECRET_KEY = getenv('SECRET')
HOST = getenv("HOST")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
DATABASE = getenv("DATABASE")

CLOUD_NAME = getenv('CLOUD_NAME')
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')