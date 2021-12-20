

def isPermutation(l1,l2):
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False