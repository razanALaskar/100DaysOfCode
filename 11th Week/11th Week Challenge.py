# Day 74 & 75: Challenge
#1:
"""
file=open("file#1.txt","rt")
print(file.read())
file.close()
file1=open("file#1.txt","a")
file1.write("\nThe best way we learn anything is by practice and exercise questions.")
file1.close()
file2=open("file#1.txt","rt")
print(file2.read())
file2.close()
"""
#2:
#2.1
import mysql.connector
#Create Database
"""
mydb=mysql.connector.connect(host="localhost",
                             user="root"
                             ,passwd="Razan0099")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE MyEmployee")
"""
#Create Table and add values
mydb=mysql.connector.connect(host="localhost",
                             user="root"
                             ,passwd="Razan0099"
                             ,database="MyEmployee")
mycursor=mydb.cursor()
"""
mycursor.execute("CREATE TABLE Employee(id INT AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(255),LastName VARCHAR(255), Age INT, Gender VARCHAR(255),Salary INT)")
sql="INSERT INTO Employee (FirstName,LastName,Age,Gender,Salary) VALUES (%s,%s,%s,%s,%s)"
values=[
    ("Ahmad","Ali",30,"Male",10000),
    ("Khalid","Muhammad",34,"Male",7000),
    ("Noura","Saleh",29,"Female",7000)]
mycursor.executemany(sql,values)
mydb.commit()
mycursor.execute("SELECT * FROM Employee")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
#2.2:
mycursor.execute("SELECT FirstName,Gender,Salary FROM Employee")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
#2.3:
mycursor.execute("SELECT * FROM Employee ORDER By FirstName DESC ")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
#2.4:
mycursor.execute("DELETE FROM Employee WHERE Age=34")
mydb.commit()
mycursor.execute("SELECT * FROM Employee")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
"""
#3:
file3=open("file#1.txt","rt")
data=file3.readlines()
for x in data:
    print(x)
