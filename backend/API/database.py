from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

parsedPassword = urllib.parse.quote_plus(os.getenv('MYSQL_PASSWORD'))

username = os.getenv('MYSQL_USERNAME')
password = parsedPassword
db_name = "ChallengeApplication"
host = "localhost"
port = "3306"

URL_DATABASE = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
