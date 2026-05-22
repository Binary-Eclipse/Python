x="hello"
print(bool(x))

#return false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(" "))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj))



#return true
print(bool(True))
print(bool("hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))


#isinstance()
x=200
print(isinstance(x,int))
print(isinstance(x,bool))
print(isinstance(x,float))