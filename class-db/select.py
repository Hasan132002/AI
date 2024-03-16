#pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = "localhost",
        database = "ramazan",
        user="root",
        password=""
        )
    if connection.is_connected():
        cursor = connection.cursor()
        select_query="Select * from student"
        cursor.execute(select_query)
        rows=cursor.fetchall()
        for data in rows:
            print(data)
except Error as e:
    print("Eror while connecting sql",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Mysql is closed")
        
        
