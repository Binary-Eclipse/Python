#tuple is ordered ,unchangable,allow duplicates 
#can't access or change the value of tuple

#but way is to convert tuple to list and then change the value and then again convert it to tuple
mytuple=("apple","banana","cherry")
mytupleList=list(mytuple) # convert tuple to list
mytupleList[1]="watermelon"
print(mytupleList)
mytuple=tuple(mytupleList)#convert list to tuple

#another way to join two tuple is to use + operator
new=("mango", )
mytuple+=new
print(mytuple)


