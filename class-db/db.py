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
        data=[
            ('Ali','ali@gamilc.opm','32442343'),
            ('Imran','imran@gmail.com','2342342'),
            ('altashonda','atlas@gmail,con','123123123')
            ]
        
        
        insert_query = "INSERT into student (name,email,contact_no)  VALUES (%s ,%s ,%s)"
        cursor.executemany(insert_query,data)
        connection.commit()
        print("Data Succesfully Inserted")
except Error as e:
    print("Eror while connecting sql",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Mysql is closed")
        
        