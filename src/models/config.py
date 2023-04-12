from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB_Name")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

SQLALCHEMY_DB_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"

engine = create_engine(SQLALCHEMY_DB_URL)
meta = MetaData()
conn = engine.connect()





