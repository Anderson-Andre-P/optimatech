import pymysql
import os
from dotenv import load_dotenv

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=os.getenv('MYSQL_PASSWORD'),
        database='ChallengeApplication',
        port=3306
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro ao conectar:", e)
finally:
    if 'connection' in locals() and connection:
        connection.close()