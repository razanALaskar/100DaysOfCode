# Day 48:Scope
#Local:Function Inside Function
def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

#Global Scope
y=350
def myfuncG():
    print(y)
myfuncG()

# Day 49:Scope2
x=350
def myfuncLG():
    x=300
    print(x)
myfuncLG()
print(x)

def myfuncGKeyW():
    global z
    z = 300

myfuncGKeyW()
print(z)

z=200
def myfuncGKeyW1():
    global z
    z = 350
myfuncGKeyW1()
print(z)

# Day 50:Modules
import mymodule
mymodule.greeting("Razan")
print(mymodule.person["Age"])

# Day 51:Modules
import mymodule as mx
print(mx.person["Name"])

import platform
print(platform.system())
print(platform.python_version())
print(dir(platform))

# Day 52:Datetime
import datetime

date=datetime.datetime.now()
print(date.year)
print(date.strftime("%A"))
date1=datetime.datetime(2020,1,1)
print(date1)
print(date1.strftime("%B"))

# Day 53 & 54: Challenge

#1:
import calculator

print(calculator.add(8,1))
print(calculator.minus(4,2))
print(calculator.multi(6,6))
print(calculator.divide(8,2))
#2:
today=datetime.datetime.now()
print(today.year)
print(today)
print(today.strftime("%B"))
print(today.strftime("%A"))

#3:
yesterday= date.today() - datetime.timedelta(days=1)
print(yesterday)
tomorrow= date.today()  + datetime.timedelta(days=1)
print(tomorrow)
