class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self) -> str:
        lists = []
        current = self.head
        while current:
            if current == self.head:
                lists.append("Head: %s" %current.data)
            elif current == self.tail:
                lists.append("Tail: %s" %current.data)
            else:
                lists.append("%s" %current.data)

            current = current.next
        return " <-> ".join(lists)


    def createDLL(self,value):
        node = Node(value)
        self.head = node
        self.tail = node

    def insertDll(self,value,location):
        if self.head is None:
            return "Empty node"

        node = Node(value)
        temp = self.head
        if location == 0:
            temp = self.head
            temp.prev = node
            self.head = node
            node.next = temp

        elif location == -1:

            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        else:
            index = 0
            while temp:
                if index < location -1:
                    temp = temp.next
                    index += 1
                else:
                    break

            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
            
    def insertion_sort_dll(self):
        if self.head is None:
            return "Empty: cant sort empty list"
        pass



dll = DoublyLinkedList()
dll.createDLL(23)
dll.insertDll(24,0)
dll.insertDll(25,1)
dll.insertDll(26,2)
dll.insertDll(27,0)
dll.insertDll(34,-1)
dll.insertDll(35,-1)


print([[x.data] for x in dll])
print(dll)