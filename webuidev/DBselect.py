import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="codethunder"
    )
mycursor=mydb.cursor()

mycursor.execute("select * from Contacts")
for z in mycursor:
    print(z)