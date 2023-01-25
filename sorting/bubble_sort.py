""" Bubble Sort
        Sorts a list of integers in an ascending order
    Args:
        my_list (list): List to be sorted 
    """

def bubble_sort(my_list):
    
    length = len(my_list)
    
    for i in range(length):
        
        for j in range(length - i -1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                
    return my_list

lisst = [3,6,393,6,8,0,5,3,2,6,4,0]
print(bubble_sort(lisst))