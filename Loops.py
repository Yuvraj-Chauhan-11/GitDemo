greeting = "Good Morning"

if greeting == "Good Morning":
    print("Good Morning")
    print("Good Morning!!")

else :
    print("Good Afteroon or Good Night")

print("if else block is completed")


# for loop

obj = [2,3,5,7,9]
for i in obj:
    print (i*4) # printing multiple of 4 of each pobject in list


# sum of first 10 natural numbers 1+2+3+4+5.....+10

# range (i,j) -> i to j-1
summation = 0
for j in range(1,11): # ()
    summation += j
print ("Sum of first 10 natural numbers is :", summation)

for k in range (1,10,4):
    print (k) # starting with 1 and using k+4 till 10-1

# now if we skip first index then by default it will treat from 0
summ = 0
for m in range (5):
    print ("m range values are:",m)

    summ = summ+m

print (summ)






