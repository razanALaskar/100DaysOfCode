# Day 55: JSON
import json
#convert to JSON:
x= { "Name":"John","Age":"30","City":"New York" }
y=json.dumps(x)
print(y)
#parse JSON
z=json.loads(y)
print(z["Age"])
#dict to JSON
print(json.dumps({ "Name":"John","Age":"30"}))
#Lis to JSON
print(json.dumps(["Apple","Banana"]))
#tuple to JSON
print(json.dumps(("Apple","Banana")))
#String to JSON
print(json.dumps("Hello"))
#int to JSON
print(json.dumps(22))
#float to JSON
print(json.dumps(5.4))
#bol to JSON
print(json.dumps(True))
#none to JSON
print(json.dumps(None))
data={
    "name":"John",
    "age":"30",
    "married":True,
    "children":("Ann","Billy"),
    "pets": None,
    "cars":[{"model":"BMW 230","mpg":27.5},
            {"model":"Ford Edge","mpg":24.1}]
}
print(json.dumps(data))
# Day 56: JSON 2
# Format the result and sorted
print(json.dumps(data,indent=4,separators=(". ","="),sort_keys=True))

# Day 57: Regular Expressions (RegEx)
import re
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("Yes! we have a match")
else:
    print("No match")

# Day 58: Regular Expressions (RegEx) 2
txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)
x1=re.findall("na",txt)
print(x1)
x2=re.search("\s",txt)
print("The first withe-space character is located in position",x2.start())
x3=re.search("na",txt)
print(x3)
x4=re.split("\s",txt)
print(x4)

# Day 59: Regular Expressions (RegEx) 3
txt="The rain in Spain"
x5=re.sub("\s","9",txt)
print(x5)
x6=re.sub("\s","9",txt,2)
print(x6)
x7=re.search(r"\bS\w+",txt)
print(x7.span())
print(x7.string)
print(x7.group())

# Day 60&61: Challenge
#1:
days=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
daysS=json.dumps(days)
print(daysS)
#2:
txt1="data is the new oil"
search=re.search("data",txt1)
print(search.group())
print(search.start())