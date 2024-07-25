import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="cspract"
)

cursor = mydb.cursor()

cursor.execute("DELETE FROM student WHERE stname='abc';")
mydb.commit()
