def isUnique(lists):
    newList = []
    for i in lists:
        if i in newList:
            print(f"NotUnique: {i} is repeated")
            return False
        else:
            newList.append(i)

    return newList == lists

lists = [1,2,3,4,5,5,6]
print(isUnique(lists))