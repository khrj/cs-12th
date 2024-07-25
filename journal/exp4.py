import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="cspract"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM student;")
rows = cursor.fetchall()
print(rows)