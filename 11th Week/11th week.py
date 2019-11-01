# Day 69: File Handling
f=open("text.txt","rt")
print(f.read())
print("/////")
f=open("text.txt","rt")
print(f.read(3))
print("/////")
f=open("text.txt","rt")
print(f.readline())
print("/////")
f=open("text.txt","rt")
for x in f:
    print(x)
f.close()
print("/////")
f1=open("text1.txt","a")
f1.write("new Line")
f1.close()
f2=open("text1.txt","r")
print(f2.read())
f2.close()
f3=open("text1.txt","w")
f3.write("woops! I have delete the content")
f3.close()
print("/////")
f4=open("text1.txt","r")
print(f4.read())
f5=open("myfile0.txt","x")
f6=open("myfile2.txt","w")
import os
if os.path.exists(("text1.txt")):
    os.remove("text1.txt")
else:print("the file doesn't exist")

# Day 70: MySQL
import mysql.connector

mydb=mysql.connector.connect(host="localhost",
                             user="root"
                             ,passwd="Razan0099")
mycursor=mydb.cursor()
#create Database
mycursor.execute("CREATE DATABASE mydatabase")
#Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
   print(x)


mydb=mysql.connector.connect(host="localhost",
                             user="root"
                             ,passwd="Razan0099"
                             ,database="mydatabase")
mycursor=mydb.cursor()

#Create Table
mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
#Create Table with primary key
mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255))")
#Check if Table Exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
#Add Primary Key to Exist Table
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# Day 71: MySQL 2
sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=("John","Highway 21")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
val=[
    ("Pater","Lowstreet 4"),
    ("Amy","Apple st 652"),
    ("Hannah","Valley 345")]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")


print("1 record inserted ID:",mycursor.lastrowid)
mycursor.execute("SELECT * FROM customers")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("SELECT name,address FROM customers")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

#Using the fetchone() Method
mycursor.execute("SELECT * FROM customers")
myresult=mycursor.fetchone()
print(myresult)

# Select With a Filter
mycursor.execute("SELECT * FROM customers WHERE address='Apple st 652'")
myresult=mycursor.fetchall()
print(myresult)
mycursor.execute("SELECT * FROM customers WHERE address LIKE '%st%'")
myresult1=mycursor.fetchall()
print(myresult1)


# Day 72: MySQL 3
#Sort the Result
mydb=mysql.connector.connect(host="localhost",
                             user="root"
                             ,passwd="Razan0099"
                             ,database="mydatabase")
mycursor=mydb.cursor()
sql= "SELECT * FROM customers ORDER BY name "
sql1= "SELECT * FROM customers ORDER BY name DESC "
mycursor.execute(sql1)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
#Delete Record
sql2= "DELETE FROM customers WHERE address ='Lowstreet 4'"
mycursor.execute(sql2)
mydb.commit()
print(mycursor.rowcount,"records deleted")
#Drop Table
mycursor.execute("DROP TABLE customers")
#Drop Table Only if Exist
mycursor.execute("DROP TABLE IF EXISTS customers")


# Day 72: MySQL 3
sql00="UPDATE customers SET address='Riyadh' WHERE address='Valley 345'"
mycursor.execute(sql00)
mydb.commit()
print(mycursor.rowcount,"Records affected")
#Limit the Result
mycursor.execute("SELECT * FROM customers LIMIT 3")
myresult11=mycursor.fetchall()
for x in myresult11:
    print(x)
# Start From Another Position
mycursor.execute("SELECT * FROM customers LIMIT 3 OFFSET 2")
myresult12=mycursor.fetchall()
for x in myresult12:
    print(x)
#JOIN
mycursor.execute("CREATE TABLE Person(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), Age INT)")
sql="INSERT INTO Person (name,age) VALUES (%s,%s)"
val=[('John', 21),
    ("Pater",30),
    ("Amy",35),
    ("Hannah",25),
    ("Razan",22)]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
sqlJoinl="SELECT Person.name AS user, customers.address AS address FROM Person LEFT JOIN customers ON Person.name = customers.name"
mycursor.execute(sqlJoinl)
myresult100=mycursor.fetchall()
for x in myresult100:
    print(x)
sqlJoinR="SELECT Person.name AS user, customers.address AS address FROM Person RIGHT JOIN customers ON Person.name = customers.name"
mycursor.execute(sqlJoinR)
myresult100=mycursor.fetchall()
for x in myresult100:
    print(x)