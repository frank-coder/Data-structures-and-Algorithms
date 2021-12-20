def findNumber(lists,num):
    for i in lists:
        if i  == num:
            print(i)
            print(lists.index(i))
myList = [1,2,3,4,5,6,6]
findNumber(myList,4)