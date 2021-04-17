import os
from dotenv import load_dotenv

dirname = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(dirname, ".env"))

DATABASE_ENDPOINT = os.environ.get("DATABASE_ENDPOINT")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
