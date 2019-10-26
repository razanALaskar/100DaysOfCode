# Day 62: PIP
import camelcase
c=camelcase.CamelCase()
text="hi everyone =)!"
print(c.hump(text))

# Day 63: Command Line Input
user= input("Enter your name:")
print("Hello",user)

# Day 64: Try-Except
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")

try:
    print("Hello")
except NameError:
    print("something wnt wrong")
else:
    print("nothing went wrong")

try:
    print(x)
except NameError:
    print("something wnt wrong")
finally:
    print("the 'try except' is finished")

# Day 65: String Formatting
price=40
txt="The price is {}$"
print(txt.format(price))
txt1="The price is {:.2f}$"
print(txt1.format(price))
quantity=3
items=33
txt2="I want {} pieces of item number {} for {:.2f}$"
print(txt2.format(quantity,items,price))

# Day 66: String Formatting 2
txt3="I want {0} pieces of item number {1} for {2:.2f}$"
print(txt3.format(quantity,items,price))
name="John"
age=20
text="His name is {1}. {1} is {0} years old."
print(text.format(age,name))
myorder="I have a {carname}, it is a {model}"
print(myorder.format(carname="Ford",model="2020"))
# Day 67&68: Challenge
#1:
fl=input("Enter the first letter of your name")
ll=input("Enter the last letter of your name")
hi="Your first letter of your name is:{} ,and last letter of your name is:{}"
print(hi.format(fl,ll))

#2:
pr=53.44
naame="Ahmad Ali"
texxt="Dear {}, Your current balance is {:.2f} $"
print(texxt.format(naame,pr))

#3:
index=int(input("Enter the number of indexes"))
mylist=list()
for i in range(index):
    x=input("Enter the value of"+str(i+1))
    mylist.append(x)
print(mylist)