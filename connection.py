import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("BD_USER")
PASSWORD = os.getenv("BD_PASSWORD")
HOST = os.getenv("BD_HOST")
PORT = os.getenv("BD_PORT")
DBNAME = os.getenv("BD_NAME")

def create_connection():
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        return connection

    except Exception as e:
        return None
