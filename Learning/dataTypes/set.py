#unordered and unindexed collection of unique items
#frozen set is immutable
#in set we can do insert,delete but in frozen set we can not do any of these

x={"apple","banana","cherry"}
x.add("orange")
print(x)
x.remove("banana")
print(x)

#but
y=frozenset({"apple","banana","cherry"})
# y.add("orange") # this will give error because frozen set is immutable

#method
r={"red","green","blue"}

#copy()
p=x.copy()
print(p)
# c=r[ :1] # this will give error because set is unordered and unindexed

#difference()
a={1,2,3,4}
b={3,4,5,6}
print(a.difference(b)) # this will give {1,2} because these are the unique items in set a

#difference_update()
a.difference_update(b)
print(a) # this will give {1,2} because these are the unique items in set a and it will update the set a

a={1,2,3,4}
b={3,4,5,6}
#intersection()
print(a.intersection(b)) # this will give {3,4} because these are the common items in set a and set b

#intersection_update()
a.intersection_update(b)
print(a) # this will give {3,4} because these are the common items in set a and set b and it will update the set a


#issubset()
a={1,2,3}
b={1,2,3,4,5}
print(a.issubset(b)) # this will give True because all items in set a are present in set b

#isssuperset()
a={1,2,3,4,5}
b={1,2,3}
print(a.issuperset(b)) # this will give True because all items in set b are present in set a

#symmetric_difference
a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b)) # this will give {1,2,5,6} because these are the unique items in set a and set b


#union 
print(a.union(b)) # this will give {1,2,3,4,5,6} because these are all the unique items in set a and set b

#update
a.update(b)
print(a)


#disjoint()

print(a.isdisjoint(b)) # this will give False because set a and set b have common items

#pop()
print(a.pop()) # this will remove and return a random item from the set a