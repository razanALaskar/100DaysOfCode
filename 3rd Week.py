# Day 13: Lists
numbers=[5,7,3.5,4,2,5]
numbers[4]=10
del numbers[3]
for x in numbers:
    print(x)

# Day 14: Lists2
L=["A","B","C","D","E"]
print(L[2:5]) #print ['C', 'D', 'E']
if "C" in L:
    print("Yes, C is there")
pyhton=["بايثون"]*4
print(pyhton) #print  ['بايثون', 'بايثون', 'بايثون', 'بايثون']
print(L+pyhton) #print ['A', 'B', 'C', 'D', 'E', 'بايثون', 'بايثون', 'بايثون', 'بايثون']

# Day 15: Lists3
print(len(L)) #print 5
L.append("G")
L.insert(5,"F")
L1=L.copy()
L.pop(5)
L.clear()
print(L) #print []
print(L1) #print  ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Day 16: Tuples
frute=("Apple", "Banana", "Cherry")
print(frute) #print ('Apple', 'Banana', 'Cherry')
LT=("A",1,1.5,"B","C","D","E")
print(LT) # print ('A', 1, 1.5, 'B', 'C', 'D', 'E')
print(LT[4]) #print C
print(LT[2:5]) #print (1.5, 'B', 'C')
del LT
# Day 17: Tuples2
f=("Apple", "Banana", "Cherry")
if "Apple" in f:
    print("Yes,Apple is there")
p=("بايثون",)*2
print(p) # print ('بايثون', 'بايثون')
print(len(p)) #print 2
print(f+p) # print  ('Apple', 'Banana', 'Cherry', 'بايثون', 'بايثون')
# Day 18&19: Challenge
newList=[1,2,3,4,5]
newList.append(6)
print(newList) #print  [1, 2, 3, 4, 5, 6]
newList.reverse()
print(newList) #print [6, 5, 4, 3, 2, 1]
print(newList.count(4)) #print 1
newList.clear()
print(newList) # print []