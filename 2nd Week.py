# Day 6: Castig
x=int("10") # convert string to integer

y=float(2) #convert integer to float

z=str(5.6) #convert float to string

# Day 7:Strings
Hi="Hello World"
print(Hi[3]) #print l
print(Hi[6:]) #print World

# Day 8: String 2
a=" Hello Wordl! "
print(a.strip()) #print Hello Wordl!
print(len(a)) #print 14
print(a.lower()) #print  hello wordl!
print(a.upper()) #print  HELLO WORDL!
print(a.replace("!","*")) #print  Hello Wordl*
print(a.split(" ")) #print ['', 'Hello', 'Wordl!', '']

#Day 9:String Format
age=23
name="John"
txt="My name is {}, and I am {}"
print(txt.format(name,age)) #My name is John, and I am 23



#Day 10:Operators

x=3*10
print(x) # print 30
y=1
y<<=4
print(y) # print 16
print(x<y) # print False

#Day 11:Operators2

print(x<8 or y>9) # print True

print(x is y) # print False
i =[5,3,2]
print(3 in i) # print True

#Day 12:

txt="Please, I want {} sandwishes and {} donutes"
txt=txt.replace("I","we")
txt=txt.format(5,7)
txt=txt.replace("a","A")
print(txt) # print PleAse, we wAnt 5 sAndwishes And 7 donutes

