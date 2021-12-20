from array import *

arr = array("i",[1,2,34,5,6,7,0])

def accessElement(array, index):
    if index > len(array) -1 :
        print("Index not found")
    else:
        print(array[index])

accessElement(arr,4)
accessElement(arr,10)
accessElement(arr,6)
accessElement(arr,7)


