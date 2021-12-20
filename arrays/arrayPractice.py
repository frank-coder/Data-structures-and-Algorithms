from array import *

#create array
print("Step 1 --Creation--")
my_array = array("i",[1,2,3,4,5,6,7,8,9])

# Array traversal
for i in my_array:
    print(i)

#Accessing individual arrays
# Araays are accessed using its index
print("Step 2 --Access--")

print(my_array[4])
print(my_array[0])

#Append value to array
#Cannot be used for appending to begining or middle of an array
print("Step 3 --Append--")
my_array.append(0)
print(my_array)

# Array insertion
#Can be used to append value anywhere in the array
print("Step 4 --Insert--")
my_array.insert(1,45)
print(my_array)

# Array extention
print("Step 5 --Extend--")
my_arrayX = array("i",[43,53,64,18])
my_array.extend(my_arrayX)
print(my_array)

# Adding to arrays from python list

print("Step 6 -- Add fromList--")
tempList = [2,4,6,8]
my_array.fromList(tempList)
print(my_array)

#Remove Array element using Pop()