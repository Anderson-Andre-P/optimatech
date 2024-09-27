from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

parsed_password = urllib.parse.quote_plus(os.getenv('MYSQL_PASSWORD'))

username = os.getenv('MYSQL_USERNAME')
password = parsed_password
db_name = os.getenv('MYSQL_DATABASE')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')

URL_DATABASE = f'mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
