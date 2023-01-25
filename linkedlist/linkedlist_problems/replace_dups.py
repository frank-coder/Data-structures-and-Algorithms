from .linkedListClass import LinkedList

def rem_dups(Llist):
    if Llist.head is None:
        return
    temp = Llist.head
    visited = set([temp.data])

    while temp.next:
        if temp.next.data in visited:
            temp.next = temp.next.next
        else:
            visited.add(temp.next.data)
            temp = temp.next
    return Llist

def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in  n:
        if pointer2 is not None:
            pointer2 = pointer2.next

        return None
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

def partition(ll)


