#!/usr/bin/python3

""" Insertion sort
    Useful for sorting a small sized list of integers
    in ascending order
    Args:
        my_list (list): list to be sorted
        
    """
def insertion_sort(my_list):
    length = len(my_list)
    
    for i in range(1, length):
        j = i
        
        while (j>0 and my_list[j-1] > my_list[j]):
            my_list[j],my_list[j-1] = my_list[j-1],my_list[j]
            
            j = j - 1
    return my_list

listt = [1,4,6,2,5,7,2,9,8]
print(insertion_sort(listt))