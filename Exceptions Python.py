from logging import raiseExceptions

ItemsInCart = 0

if ItemsInCart !=2:
    #   raise Exception("product cart count mismatched")
    pass # in this case if condition does nothing


assert (ItemsInCart ==0) # assert always expect pass condition otherwise it ll give error



# try, catch(except)

try:
    with open('test1.txt', 'r') as reader:  # test1 file not present , if present it then it exceutes succesfully.
        reader.read()

except:
    print('An error occurred')


try:
    with open('test1.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)



# finally --> only use when we have try and except mechanism and always exceutes even if

finally:
    print("cleaning the data")



