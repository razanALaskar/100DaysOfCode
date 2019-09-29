# Day 41:Classes and Objects
class myClass:
    x=4
x=myClass()
print(x.x)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("Razan",24)
print(p.name)
print(p.age)
# Day 42:Classes and Objects 2
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printInfo(self):
        print("Hello my name is ",self.name)
p=person("Razan",24)
p.printInfo()
p.age=20
print(p.age)
del p.age
del p
# Day 43:Inheritance
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printInfo(self):
        print(self.fname+self.lname)
p1=person("Razan","Fahad")
p1.printInfo()
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
s=student("Hamad","Fahad")
s.printInfo()
# Day 44:Inheritance 2
class student1(person):
    def __init__(self,fname,lname,graduationyear):
        super().__init__(fname,lname)
        self.graduationyear=graduationyear
    def welcome(self):
        print("Welcome",self.fname,self.lname,"to the class of",self.graduationyear)
s=student1("Hamad","Fahad",2019)
s.printInfo()
print(s.graduationyear)
s.welcome()
# Day 45:Iterators
fruits=("Apple","Orange","Banana")
it=iter(fruits)
print(next(it))
print(next(it))
print(next(it))
app="Apple"
itr=iter(app)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
for x in fruits:
    print(x)
for x in app:
    print(x)

# Day 46 & 47: Challenge
class Library:
    def __init__(self,book,shelf):
        self.book=book
        self.shelf=shelf
l1=Library(300,45)
class science_section(Library):
    def __init__(self, book, shelf,name):
        super().__init__(book,shelf)
        self.name=name
sc=science_section(300,45,"Physics books")
print(sc.book)
print(sc.shelf)
print(sc.name)
sc.book=20
sc.shelf=4
print(sc.book)
print(sc.shelf)