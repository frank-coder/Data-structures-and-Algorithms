#!/usr/bin/python3

""" Quick Sort
    Sorts an array of integers in ascending order
    using the quick sort algorithm
    
    Args:
        my_list (list): python list to be sorted
        low (int): lowest bound index
        high (int): upper bound index
    """
    
def quick_sort(my_list, low, high):
    
    if (low < high):
        part = partition(my_list, low, high)
        print(part)
        
        #befort part
        quick_sort(my_list, low, part - 1)
        
        #after partition
        quick_sort(my_list, part + 1, high)
        

def partition(rec_list, low, high):
    """ Partition
        This implementation utilizes pivot as the last element in the nums list
        It has a pointer to keep track of the elements smaller than the pivot
        At the very end of partition() function, the pointer is swapped with the pivot
        to come up with a "sorted" nums relative to the pivot
        
        Args:
            rec_list (list): list to be partitioned 
            low (int): lowest bound index
            high (int): upper bound index
            
        """
        
    pivot = rec_list[high]
    i = low - 1
    
    for j in range(low, high):
        if rec_list[j] <= pivot:
            
            i = i + 1
            
            #Swap
            rec_list[i],rec_list[j] = rec_list[j], rec_list[i]
            #print(rec_list)
            
    # Swap the pivot element with the greater element specified by i
    (rec_list[i + 1], rec_list[high]) = (rec_list[high], rec_list[i + 1])
 
    # Return the position from where partition is done
    return i + 1

lisst = [4,3,6,3,8,9,0,1,34]
size = len(lisst)
quick_sort(lisst, 0, size - 1)

print(lisst)