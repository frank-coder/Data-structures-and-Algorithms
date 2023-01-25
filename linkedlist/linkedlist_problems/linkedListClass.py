from random import randint

class Node:
    def __init__(self,value) -> str:
        self.data = value
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        temp = self.head
        index = 0
        while temp:
            temp = temp.next
            index += 1
        return index

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __str__(self):
        all = [str(x.data) for x in self]
        return " -> ".join(all)

    def add(self,nodeValue):
        node = Node(nodeValue)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        temp = self.tail
        self.tail.next = node
        self.tail = node

    def generate(self,n,min_val,max_val):
        for x in range(n):
            self.add(randint(min_val,max_val))
        return



sl = LinkedList()
sl.generate(6,1,100)
print(len(sl))

#print([x.data for x in sl])
print(sl)