## declaration
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
mylist=["apple","banana","cherry"]

##length of list
print(len(mylist))

#  list can contain multiple datatypes
mylist1=["hello",1,False,2.50,("apple","banana"),["apple","banana"],{"name":"tutul","age":24}]
print(mylist1)

##list type()
print(type(mylist1))


## change list
thislist=["apple","banana","cherry"]
thislist[1]="watermelon"
print(thislist)
thislist[1:3]=["banana","green"]
print(thislist)

##insert
itemlist=["apple","banana","cherry"]
itemlist.insert(2,"watermelon")
print(itemlist)

##append
itemlist.append("mango")
print(itemlist)

##extend
digit=["1","2","3"]
itemlist.extend(digit)
print(itemlist)


##remove
itemlist.remove("banana")
print(itemlist)

itemlist.pop(0)
print(itemlist)

del thislist[0]
print(thislist)

thislist.clear()
print(thislist)



##for loop

for x in itemlist:
    print(x)

for i in range(len(itemlist)):
    print(itemlist[i])



##shorthand loop
[print(x) for x in itemlist]
newlist=[x for x in itemlist if "a" in x]
print(newlist)


## while loop

itemlist=["apple","banana","cherry"]
i=0
while i<len(itemlist):
    print(itemlist[i])
    i+=1


## sort
itemlist=["Banana","cherry","apple"]
digit=[10,7,9,1,5,3,8,2,4,6]

# sort() method is case sensitive,resulting in all capital letters being sorted before lower case letters:
itemlist.sort()
print(itemlist)
#instead
itemlist.sort(key=str.lower)
print(itemlist)


digit.reverse()
print(digit)
digit.sort(reverse=True)
print(digit)





##copy list
mylist=["apple","banana","cherry"]
mylist2=mylist.copy()
print(mylist2)

mylist3=mylist2[ : ]
print(mylist3)

#built in function
mylist4=list(mylist)
print(mylist4)

## join list
list1=["a","b","c"]
list2=[1,2,3]
#using operator
list3=list1+list2
print(list3)

#with loop
for x in list2:
    list1.append(x)
print(list1)

#without looop
list1.extend(list2)
print(list1)