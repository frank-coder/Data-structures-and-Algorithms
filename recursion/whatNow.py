def missingNumber(lists):
    sums = sum(lists)
    #print(sums)
    missing = 0
    for i in range(1,len(lists) + 2):
        missing += i
        #print(missing)

    return missing - sums


print(missingNumber([1,2,3,4,6,7,8]))