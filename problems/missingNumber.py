#! usr/bin/python3

#Given a list of numbers, find the missing number

#formula for solving this problem is n*n+1/2

myList = [1,2,3,4,5,6,7,8,10,11,12]

def findMissing(lists,n):
    sum1 = n*(n+1)/2
    sum2 = sum1-sum(lists)

    return sum2

print(findMissing(myList,12))