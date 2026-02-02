file = open('test.txt')

# read all the content of files
# print(file.read())
# read n number of characters by passing parameter
 # print(file.read(13))
# read line by line in file and also do not mix raed by line and raed by character for clear output as its rare scenario
# print(file.readline())
# print(file.readline())



# print line by line using readline method
#line = file.readline()
#while line!="":
 #  print(line)
  # line = file.readline()
#file.close()




# file.close()
# readlines method --> each line will be stored as list as seen earlier and we can simply iterate using for loop to print.

for line in file.readlines():
    print (line)