import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345678',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All done...")