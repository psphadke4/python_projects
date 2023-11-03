import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='####',
    password='######'
)

cursorObject= database.cursor()

cursorObject.execute("CREATE DATABASE crm")
print("ALL DONE!!")
