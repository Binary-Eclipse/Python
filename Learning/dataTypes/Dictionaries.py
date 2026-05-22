thisdict={
    "a": "apple",
    "b": "banana",
    "age": 30
}

print(thisdict)
print(thisdict["a"])
print(thisdict.get("b"))

##any datatype can store like list

#get keys & values separately
print(thisdict.keys())
print(thisdict.values())

print("\nrepresentation of item() function\n")
#get items
print(thisdict.items()) # this will give a list of tuples where each tuple is a key-value pair

#loop through dictionary
for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

print("\nrepresentation of item() function\n")
for x,y in thisdict.items():
    print(x,y)


##add
thisdict["c"]="cherry"
print(thisdict)


##update
thisdict.update({"m":"mango"})
print(thisdict)


##nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child1"]["name"])


#You can loop through a dictionary by using the items() method like this:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])