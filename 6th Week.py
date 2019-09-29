# Day 34: Functions 2
def print_array(food):
    for x in food:
        print(x)
fruits=["Apple","Orange"]
print_array(fruits)
def multip(x):
    return 5*x
print(multip(4))
def print_name(*name):
    print("The name is:",name[1])
print_name("Razan","Rana")
def rec(k):
    if(k>0):
        result=k+rec(k-1)
        print(result)
    else:
        result=0
    return result
rec(5)
# Day 35:Lambda
x= lambda a:a+10
print(x(1))
y=lambda a,b: a*b
print(y(4,5))
z=lambda a,b,c: a+b+c
print(z(4,5,6))
# Day 36:Lambda 2
def fun(n):
    return lambda a : a*n
xx=fun(5)
yy=fun(5)
print(yy(3))
print(xx(4))
# Day 37:Arrays
cars=["BMW","Toyota","Ford"]
print(cars[0])
cars[0]="Lxuz"
print(cars[0])
print(len(cars))
# Day 38:Arrays
for x in cars:
    print(x)
cars.append("Honda")
print(cars)
cars.pop(2)
print(cars)
cars.remove("Toyota")
print(cars)
# Day 39 & 40: Challenge
#1:
def rec3 (n,l):
    if(n>0):
        return l*rec3(n-1,l)
    else:
        return 1
print(rec3(3,5))
#2:
l=[88, 9, 7, 3, 2,-1,-5,-6,-4]
listxx= list(filter( lambda x: (x >= 0),l))
print(*listxx)