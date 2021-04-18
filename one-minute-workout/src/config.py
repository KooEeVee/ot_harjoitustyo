import os
from dotenv import load_dotenv

dirname = os.path.dirname("src/.env")

load_dotenv(os.path.join(dirname, ".env"))

DATABASE_ENDPOINT = os.environ.get("DATABASE_ENDPOINT")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
