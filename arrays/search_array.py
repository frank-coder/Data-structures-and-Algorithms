from array import *

arr = array("i",[1,2,34,5,6,7,0])

def search_array(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "the element does not exist"

print(search_array(arr,6))
print(search_array(arr,10))
