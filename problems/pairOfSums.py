
#Leetcode Two Sums

def findPairs(nums,target):
    print(f"Sum of number pairs that add up to {target}:")
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(f"Sum of: {nums[i]},{nums[j]} indices {i},{j}")


mylist = [1,2,4,5,4,2,3,6,4,3,5,6]
findPairs(mylist,9)