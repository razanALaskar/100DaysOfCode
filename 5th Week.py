# Day 27: Conditional Statements If..else
a=200
b=150
if a > b:
    print("a greater than b")
elif b > a:
    print("b greater than a")
else:
    print("a equal b")
c=20
d=20
if c == d: print("c and d are equal")
print("A")if a > b else print("B") if a == b else print("A B")
if a > b and c >= d:
    print("True")
if a > b or c >= d:
    print("True also")
if c > 10:
    print("Above 10")
    if c >20:
        print("Above 20")
# Day 28: Loops: While Loop
i=1
while i <6:
    print(i)
    if i==3:
        break
    i+=1
while i <6:
    i += 1
    print(i)
    if i==3:
        continue
else:
    print("i equals 6")
# Day 29: Loops2: For Loop
fruits=["Apple","Orange","Banana"]
for x in fruits:
    print(x)
for x in "Razan":
    if x == "z":
        continue
    print(x)
for x in "Razan":
    print(x)
    if x == "z":
        break
# Day 30: Loop3: For Loop
for x in range(6):
    print(x)
print("_________________")
for x in range(3,7):
    print(x)
print("_________________")
for x in range(2,7,2):
    print(x)
else:
    print("Finally finished")
print("_________________")
for x in range(1,5):
    for i in range(1,3):
        print("x=",x,"i=",i)
# Day 31: Functions
def myFun():
    print("Hello My World")
myFun()
def myFun1(name="User"):
    print("Hello",name,"!")
myFun1("Razan")
myFun1("Rawan")
myFun1()
# Day 32 & 33: Challenge
for a in range(3,18,2):
    print(a)
    for b in range(2,17,2):
        print(b)