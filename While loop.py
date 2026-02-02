# while loop will keep on run till the condition becomes false but in for loop we defined how long the loop should run.

it = 4
while it>1:
    if it !=3:
        print (it)
    it = it-1

print ('while loop execution is done')

# break

it = 6
while it>1:
    if it == 3:
        break
    print (it)
    it = it-1

print ('while loop execution is done')

# continue

it = 10
while it>1:
    if it == 9:
        it = it-2
        continue
    if it == 3:
        break
    print (it)
    it = it-1

print ('while loop execution is done')