from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PORT = os.environ.get("DB_PORT")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME") 
DB_PASS = os.environ.get("DB_PASS")

SECRET_KEY = os.environ.get("SECRET_KEY")