values = [1,2,"rahul",5,4]
# List is a data type that allows multiple values and can be different data types
print(values[0]) # 1
print(values[-1]) # 4 -- which is last index value of list
print (values[1:3]) # 2 , rahul , last one will not be print and rest 1 to 2 will be printed
values.insert (3, "singh") # for insertion of  values after index 2
print(values) # print the new list of values.
values.append("Final") # add values to the list in the last
print (values)
values[2] = 'yuvraj' # update list of values.
print (values)
del values[0] # delete from the list
print (values)

# tuple

fruits = ("apple", "banana", "cherry", "date", "elderberry")
# we can n ot  odify /add new va;lues to the tuple datatype list as its enclosed in round brackets , thats the only difference from list data type.

print(fruits[0])
# fruits[2] = 'yuvraj' # not supported
print(fruits[-1])
print (fruits[1:3])

# dictionary
dic = {"r" : "2" , 4 : "bcd", "v" : "test" }

print (dic["r"])
dic["last"] = "Final"
print (dic)