def findMaxProduct(lists):
    maxi = 0
    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            if lists[i] * lists[j] > maxi:
                maxi = lists[i] * lists[j]

    return maxi

def findMaxProduct2(lists):
    lists.sort()
    maxp = 0
    leftPointer = 0
    rightPointer = len(lists) -1

    while leftPointer != rightPointer:
        if lists[leftPointer] * lists[rightPointer] >= maxp:
            maxp = lists[leftPointer] * lists[rightPointer]
            leftPointer += 1
            print(lists[leftPointer])

        elif lists[leftPointer] * lists[rightPointer] <= maxp:
            rightPointer -= 1
            print(lists[rightPointer])


    return maxp

myList = [-1,2,3,4,5,6,7,8,9]
print(findMaxProduct(myList))
print(findMaxProduct2(myList))