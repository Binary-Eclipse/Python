##1 String Declaration
name="Shakil"
print(name)

##2 loop through  the letters

for x in "banana":
    print (x)


##3 string length

a="hello world"
print(len(a))

##4 check string is exist in the string or not

txt="The best things in life are free!"

print("free" in txt)
print("lot" not in txt)


##5 slicing

 # b[start:end:step] start to end-1

b="Hello World"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2]) # negative indexing


##6 modify String

a="hello, world"

print(a.upper())
print(a.lower())


##7 remove white space
a=" hello, world "
print(a.strip()) # removes whitespace from the beginning and end of the string


##8 replace string

a="hello, world"
print(a.replace("h","j"))


##9 split
a="hello, world"
print(a.split(",")) # returns a list where the string has been split at each comma

##10 concatenate string
a="hello"
b="world"
print(a+" "+b)


##10 String Format

age=36
txt=f"My name is John, and I am {age} years old"
print(txt)

tox="My name is John, and I am {} years old"
print(tox.format(age))

price=200.344
tp=f"the price of the item is {price:.2f} takas"
print(tp)
tp="the price of the item is {:.2f} takas"
print(tp.format(price))