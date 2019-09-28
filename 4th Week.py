# Day 20: Sets
thisset ={"Apple","Orange","Banana","Apple"}
print(thisset)
for x in thisset:
    print(x)
print("Banana is in the set:",("Banana"in thisset))
thisset.add("Cherry")
thisset.update(["Mango","Grapes"])
print(thisset)
# Day 21: Sets2
print(len(thisset))
thisset.remove("Apple")
thisset.discard("Orange")
print(thisset)
thisset.clear()
print(thisset)
# Day 22: Dictionaries
cars={"Model":"Ford","Year":"2018"}
print(cars)
print(cars["Year"])
print(cars.get("Model"))
cars["Year"]="2019"
print(cars)
for x in cars:
    print(cars[x])
for x in cars.values():
    print(x)
for x in cars.items():
    print(x)
# Day 23: Dictionaries2
if "Model" in cars:
    print("Model is in dictionary")
print(len(cars))
cars["Color"]="Blue"
print(cars)
cars.pop("Year")
print(cars)
cars.clear()
print(cars)
del cars
# Day 24: Dictionaries3
cars={"Model":"Ford","Year":"2018"}
cars1=cars.copy()
cars2= dict(cars)
print(cars1)
myfaily={
    "Child1":{"Name":"Rana",
              "Age":"18"},
    "Child2":{"Name":"Ruba",
              "Age":"16"}
}
print(myfaily)
cars4=dict(Model="Ford",Year="2018")
print(cars4)
# Day 25 & 26: Challenge
#1:
set = {1, 3, 5, 7, 8}
set.update([4,8,12])
print(set)
set.discard(8)
print(set)
set.clear()
print(set)
#2:
dic={"name":"pigeon","type":"bird","skin cover":"feathers"}
print(dic["type"])
dic["skin cover"]="colorful feathers "
print(dic)