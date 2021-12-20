def findMaxProduct(lists):
    maxi = 0
    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            if lists[i] * lists[j] > maxi:
                maxi = lists[i] * lists[j]

    return maxi

myList = [1,2,3,- 4,5,6,7,8,-9]
print(findMaxProduct(myList))